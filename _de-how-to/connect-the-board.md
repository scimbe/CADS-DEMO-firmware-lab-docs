---
title: Board anschließen
order: 1
description: Browser-Voraussetzungen, der Geräte-Dialog und was macOS, Windows und Linux brauchen, bevor die ST-Link aus dem Browser nutzbar ist
---

Das Board steckt an deinem eigenen Rechner, und der Browser spricht mit WebUSB (ST-Link,
Flashen und Debuggen) und WebSerial (die Konsole) mit ihm. Der Container sieht das USB-Gerät nie.

## Browser

| Browser | Funktioniert | Hinweis |
|---|---|---|
| Google Chrome | ja | WebUSB und WebSerial sind verfügbar. |
| Microsoft Edge | ja | Gleiche Engine wie Chrome. |
| Chromium, Brave, Vivaldi, Opera | meist | Chromium-basiert; manche Builds schalten die Geräte-APIs ab. Im Zweifel mit `chrome://device-log` prüfen. |
| Firefox | nein | Kein WebUSB, kein WebSerial. |
| Safari | nein | Kein WebUSB, kein WebSerial. |

Das Labor muss über **HTTPS** ausgeliefert werden (oder von `localhost`/`127.0.0.1` bei einem
lokalen Container). Chromium stellt `navigator.usb` und `navigator.serial` nur auf sicheren
Origins bereit. Das produktive Labor sitzt hinter einem TLS-Edge, das betrifft also nur selbst
gehostete Kopien.

Von Firma oder Hochschule verwaltete Browser können die APIs per Richtlinie sperren
(`DefaultWebUsbGuardSetting`, `DefaultSerialGuardSetting`). Symptom: der Geräte-Dialog öffnet
sich nie. Prüfe `chrome://policy`.

## Kabel und Port

Nutze den **ST-Link-USB-Port** des NUCLEO-Boards (den Micro-USB-Anschluss am ST-Link-Teil des
Boards, am gegenüberliegenden Ende der Ethernet-Buchse), nicht den User-USB-Port. Das eine Kabel
trägt sowohl den SWD-Debug-Link als auch den virtuellen COM-Port.

Das Gerät, das der Dialog zeigt, ist *STM32 STLink*, Vendor-ID `0x0483`, Product-ID `0x374B`
(ST-Link/V2-1).

## Verbinden

1. Logge dich ein und öffne den Workspace.
2. Klicke den Statusleisten-Eintrag **Board: getrennt** und wähle *Board verbinden (USB/Serial
   freigeben)*, oder führe **F1 → CaDS Board: Verbinden** aus.
3. Wähle im USB-Dialog *STM32 STLink*, dann im seriellen Dialog den COM-Port der ST-Link.
4. Die Statusleiste wechselt auf **Board: verbunden · läuft**.

Der Geräte-Dialog ist ein Browser-Dialog und braucht einen Klick von dir; nichts im Labor kann
ihn von selbst öffnen. Beide Freigaben werden je Origin gespeichert, sodass die nächste Sitzung
und jedes Aus- und Wiedereinstecken ohne Dialog neu verbinden (siehe
[Wiederverbinden nach Replug]({{ '/de/how-to/reconnect-after-replug/' | relative_url }})).

## macOS

- Kein Treiber nötig. Die ST-Link erscheint als USB-Gerät und als Port `/dev/cu.usbmodem…`.
- macOS mountet bei jedem Einstecken das Massenspeicher-Laufwerk **`NOD_F429ZI`** des Nucleo und
  schreibt ungefragt Metadaten hinein. Die ST-Link interpretiert Schreibzugriffe auf dieses
  Laufwerk als Firmware für `0x08000000`; das cads-zero-Projekt hat daraus eine echte
  Flash-Korruption dokumentiert (ein gelöschtes Bit im initialen Stackpointer, Board hängt in
  `Reset_Handler`). Hänge es nach jedem Einstecken aus:

  ```bash
  diskutil list external            # find the disk number N
  diskutil unmountDisk /dev/diskN
  ```

  Eine dauerhafte Lösung ist ein `/etc/fstab`-Eintrag `LABEL=NOD_F429ZI none msdos rw,noauto`
  (braucht sudo). Zeigt das Board nach einem Einstecken jemals wild leuchtende LEDs, flashe es
  neu, bevor du theoretisierst.

## Windows

- WebUSB unter Windows kann nur Geräte öffnen, die an den generischen WinUSB-Treiber gebunden
  sind. Listet Chromes Dialog die ST-Link nicht, hat ein Herstellertreiber (ST-Link,
  STM32CubeProgrammer) das Debug-Interface belegt; schalte dieses Interface mit Zadig oder dem
  Geräte-Manager auf WinUSB um.
- Der COM-Port erscheint als `STMicroelectronics STLink Virtual COM Port (COMx)`.

## Linux

- Der Browser braucht Lese- und Schreibzugriff auf den USB-Geräteknoten. Installiere die
  Standard-udev-Regel von stlink und stecke neu ein:

  ```bash
  sudo tee /etc/udev/rules.d/49-stlinkv2-1.rules >/dev/null <<'EOF'
  SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="374b", MODE:="0666", TAG+="uaccess"
  EOF
  sudo udevadm control --reload-rules && sudo udevadm trigger
  ```

- Der serielle Port ist `/dev/ttyACM0` (oder höher). Dein Benutzer muss in der Gruppe `dialout`
  sein (`plugdev` bei manchen Distributionen), um ihn zu öffnen. Nach dem Hinzufügen ab- und
  wieder anmelden.
- Als Snap oder Flatpak paketierte Browser sehen USB-Geräte möglicherweise gar nicht; nutze das
  Distributionspaket oder das `.deb` des Herstellers.

## Prüfen

`st-info --probe` im integrierten Terminal druckt bei verbundenem Board die Seriennummer der
ST-Link, `chipid 0x419` (STM32F42x/F43x) und die Flash-Größe, und ohne Board den Hinweis
`Board-Bridge nicht aktiv – Board im Browser verbinden (CaDS Board Panel)`.
