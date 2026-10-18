# Samsung ExLink for Q-SYS

Control Samsung consumer TVs through ExLink, including power, volume, inputs,
remote keys, and Frame Art Mode. Use a Q-SYS serial port or a raw TCP serial
gateway. Target Designer/Core version: **10.5**.

**Package 1.1.0.3** contains plugin **1.1.0.3**, including the connection-status corrections. The Samsung package icon is unchanged. Native Designer rendering, Core and physical-TV acceptance remain open.

## Install with Q-SYS Library

1. Sign in to [Q-SYS Library](https://library.qsys.com/my-library).
2. Open **My Packages → Add Personal Package**.
3. Enter **Samsung Consumer ExLink** and this package URL:

   ```text
   https://joshua-small.github.io/qsys-samsung-exlink/registration/joshuasmall.qsys.samsungexlink/index.json
   ```

4. In Designer, sign in with the same QSC ID and open **Tools → Show Asset Installer**.
5. Refresh **Available Assets**, select this package, and install it.
6. Add **Samsung → Consumer ExLink** to your design.

For manual installation, download `SamsungExLink.qplug` from
[Releases](https://github.com/joshua-small/qsys-samsung-exlink/releases) and place
only that file in your Documents folder under `QSC/Q-Sys Designer/Plugins`.
Use one installation method to avoid duplicate copies.

## Connect

### Serial

1. Leave **Connection Type = Serial** and **Baud Rate = 9600**.
2. Add your Q-SYS device's Serial Port component and wire it to the plugin's
   **Serial** input.
3. Connect the physical RS-232 port to the TV's ExLink connector. Use **9600 baud,
   8 data bits, no parity, 1 stop bit**. Pair transmit with receive and ground
   with ground; check your adapter's pinout.
4. Save the design to the Core and run it. Physical serial communication requires
   a Core; it is not available in Designer emulation.
5. Send a command and check the TV and the diagnostics on **Setup**.

### TCP

Select **Connection Type = TCP**, enter **TCP Address**, and set **TCP Port**
(default **1515**). The endpoint must accept raw binary ExLink packets. This is
not Samsung MDC, WebSocket, or authenticated IP control. Direct TV support
depends on the model; a compatible serial gateway can supply the TCP endpoint.

Use **Reconnect** after a connection failure. Reconnect clears pending commands;
commands are never replayed automatically. Switching back to Serial requires
checking the Serial input wiring.

## Use

| Page | Controls |
| --- | --- |
| Setup | Connection status, reconnect, clear queue, and communication diagnostics |
| Controls | Power, volume, mute toggle, HDMI/input selection, Art/Ambient modes, picture and sound presets |
| Remote | Navigation, digits, channel controls, playback, color keys, and additional remote keys |

Buttons send commands. For a selected input, key, or preset, choose the value
then press **Send/Apply**. The volume fader sends when changed. No power or volume
command is sent just because the plugin starts or reconnects.

For UCI or scripting control, expose the required pins in component Properties.
Selection pins must be set before pulsing their Send/Apply pins.

The plugin does not read back power, input, volume, mute, or Art Mode state.
Selections are command targets. A green communication status means a success
reply was received, not that the TV is on. Available commands depend on the TV.

## Timing and troubleshooting

| Property | Default | Use |
| --- | --- | --- |
| Reply Handling | Monitor only | Sends paced commands without requiring replies |
| Command Interval | 0.3 seconds | Increase if commands are missed |
| Power On Delay | 5 seconds | Time allowed before the next command after power-on/toggle |
| Reply Timeout | 2 seconds | Applies when Reply Handling is Wait for success |

Enable **Show Debug**, then set **Debug Print = Tx/Rx** to see transmitted and
received bytes. Check **Last response** on Setup. If using **Wait for success**,
a timeout clears pending commands and requires **Reconnect**. Keep **Monitor
only** for command-only wiring or TVs that do not reliably acknowledge commands.

## Updates

Refresh the package from its menu in Library's **My Packages** tab, or allow its
daily refresh. In Designer, refresh **Available Assets** and install the update.
For an existing design, use **Design Assets → Update Selected**, check the design,
then save and deploy it when appropriate. Installing an asset on your PC does
not update running Cores automatically.

Independent plugin; not endorsed by Samsung or Q-SYS. For help or bug reports,
[open an issue](https://github.com/joshua-small/qsys-samsung-exlink/issues) with
your TV model, firmware, Designer version, connection type, and observed result.
