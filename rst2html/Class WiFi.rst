############
Class WiFi
############

**Description**

Defines a class of WiFi and network implementation for Ameba.

**Syntax**

  class WiFiClass

**Members**

+-----------------------------------------------------------+--------------------------------------+
| **Public Constructors**                                   |                                      |
+-----------------------------------------------------------+--------------------------------------+
| `WiFiClass::WiFiClass <#WiFiClass_WiFiClass>`_            | Constructs a WiFiClass object and    |
|                                                           | initializes the WiFi libraries and   |
|                                                           | network settings                     |
+-----------------------------------------------------------+--------------------------------------+

.. +------------------------------+--------------------------------------+
.. | **Public Constructors**      |                                      |
.. +------------------------------+--------------------------------------+
.. | WiFiClass::WiFiClass         | Constructs a WiFiClass object and    |
.. |                              | initializes the WiFi libraries and   |
.. |                              | network settings                     |
.. +------------------------------+--------------------------------------+
.. | **Public Methods**           |                                      |
.. +------------------------------+--------------------------------------+
.. | WiFiClass::firmwareVersion   | Get firmware version                 |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: begin            | Start Wifi connection for OPEN       |
.. |                              | networks                             |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: config           | Configure network IP settings        |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: setDNS           | Set the DNS server IP address to use |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: disconnect       | Disconnect from the network          |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: macAddress       | Get the interface MAC address        |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: localIP          | Get the interface IP address         |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: subnetMask       | Get the interface subnet mask        |
.. |                              | address                              |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: gatewayIP        | Get the gateway IP address           |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: SSID             | Return the current SSID associated   |
.. |                              | with the network                     |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: BSSID            | Return the current BSSID associated  |
.. |                              | with the network                     |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: RSSI             | Return the current RSSI (Received    |
.. |                              | Signal Strength in dBm) associated   |
.. |                              | with the network                     |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: encryptionType   | Return the Encryption Type           |
.. |                              | associated with the network          |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: scanNetworks     | Start scan WiFi networks available   |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: SSID             | Return the SSID discovered during    |
.. |                              | the network scan                     |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: encryptionType   | Return the encryption type of the    |
.. |                              | networks discovered during the       |
.. |                              | scanNetworks                         |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: encryptionTypeEx | Return the security type and         |
.. |                              | encryption type of the networks      |
.. |                              | discovered during the scanNetworks   |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: RSSI             | Return the RSSI of the networks      |
.. |                              | discovered during the scanNetworks   |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: status           | Return Connection status             |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: hostByName       | Resolve the given hostname to an IP  |
.. |                              | address                              |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: apbegin          | Start AP mode                        |
.. +------------------------------+--------------------------------------+
.. | WiFiClass:: disablePowerSave | Disable power-saving mode            |
.. +------------------------------+--------------------------------------+

-----

- WiFiClass::WiFiClass

**Description**

Constructs a WiFiClass object and initializes the WiFi libraries and
network settings.

**Syntax**

WiFiClass::WiFiClass()

**Parameters**

The function requires no input parameter.

**Returns**

The function returns nothing.

**Example Code**

NA

**Notes and Warnings**

An instance of WiFiClass is created as WiFi inside WiFi.h and is
extern for direct use.

-----

- WiFiClass::firmwareVersion


**Description**

Get firmware version

**Syntax**



  char* WiFiClass::firmwareVersion()

**Parameters**

The function requires no input parameter.

**Returns**

WiFi firmware version

**Example Code**

Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

**Notes and Warnings**

NA

-----

- WiFiClass::begin


**Description**

Start Wifi connection for OPEN networks

**Syntax**

  int begin(char* ssid)

  int begin(char* ssid, uint8_t key_idx, const char* key)

  int begin(char* ssid, const char* passphrase)

**Parameters**

ssid : Pointer to the SSID string

key_idx : The key index to set. Valid values are 0-3.

key : Key input buffer.

passphrase: Passphrase. Valid characters in a passphrase must be
between ASCII 32-126 (decimal).

**Returns**

WiFi status

**Example Code**

Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

**Notes and Warnings**

NA

-----

- WiFiClass::config


**Description**

Configure network settings for the WiFi network

**Syntax**



  void WiFiClass::config(IPAddress local_ip)

  void WiFiClass::config(IPAddress local_ip, IPAddress dns_server, IPAddress gateway)

  void WiFiClass::config(IPAddress local_ip, IPAddress dns_server, IPAddress gateway, IPAddress subnet)

**Parameters**

local_ip : Local device IP address to use on the network

dns_server : IP address of the DNS server to use

gateway : IP address of the gateway device on the network

subnet : Subnet mask for the network, expressed as a IP address

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

This will disable the DHCP client when connecting to a network, and
will require the network accepts a static IP. The configured IP
addresses will also apply to AP mode, but the DHCP server will not be
disabled in AP mode.

-----

- WiFiClass::setDNS


**Description**

Configure the IP address of the DNS server to use

**Syntax**



  void WiFiClass::setDNS(IPAddress dns_server1)

  void WiFiClass::setDNS(IPAddress dns_server1, IPAddress dns_server2)

**Parameters**

dns_server1: IP address of DNS server to use

dns_server2 : IP address of DNS server to use

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“WiFi.h” must be included to use the class function.

-----

- WiFiClass::disconnect


**Description**

Disconnect from the network

**Syntax**

int disconnect (void);

**Parameters**

The function requires no input parameter.

**Returns**

The function returns one value of wl_status_t enum as an integer.

**Example Code**

NA

**Notes and Warnings**

“WiFi.h” must be included to use the class function.

-----

- WiFiClass::macAddress


**Description**

Get the interface MAC address

**Syntax**

uint8_t* macAddress(uint8_t* mac);

**Parameters**

mac : an array to store MAC address

**Returns**

The function returns a pointer to uint8_t array with length
WL_MAC_ADDR_LENGTH.

**Example Code**

Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

**Notes and Warnings**

“WiFi.h” must be included to use the class function.

------

- WiFiClass::localIP


**Description**

Get the interface IP address

**Syntax**

IPAddress localIP(void);

**Parameters**

NA

**Returns**

This function returns the IP address of the interface.

**Example Code**

Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

**Notes and Warnings**

“WiFi.h” must be included to use the class function.

------

- WiFiClass::subnetMask


**Description**

Get the interface subnet mask address

**Syntax**

  IPAddress WiFiClass::subnetMask()

**Parameters**

The function requires no input parameter.

**Returns**

subnet mask address value

**Example Code**

Example: ConnectNoEncryption
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectNoEncryption/ConnectNoEncryption.ino)

**Notes and Warnings**

NA

-----

- WiFiClass::gatewayIP


**Description**

Get the gateway IP address

**Syntax**

IPAddress gatewayIP(void);

**Parameters**

NA

**Returns**

The function returns the value of the gateway IP address.

**Example Code**

Example: ConnectNoEncryption
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectNoEncryption/ConnectNoEncryption.ino)

**Notes and Warnings**

NA

------

- WiFiClass::SSID


**Description**

Return the current SSID associated with the network

**Syntax**

char* SSID(void);

**Parameters**

NA

**Returns**

The function returns current SSID associate with the network.

**Example Code**

Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

**Notes and Warnings**

“WiFi.h” must be included to use the class function.

------

- WiFiClass::BSSID


**Description**

Return the current BSSID associated with the network

**Syntax**

uint8_t* BSSID(uint8_t* bssid);

**Parameters**

bssid : an array to store bssid

**Returns**

This function returns the uint8_t array storing BSSID with length WL_MAC_ADDR_LENGTH (6 bit).

**Example Code**

Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

**Notes and Warnings**

NA

------

- WiFiClass::RSSI


**Description**

Return the current RSSI (Received Signal Strength in dBm) associated
with the network

**Syntax**

int32_t RSSI(void);

**Parameters**

NA

**Returns**

The function returns a signed-value signal strength

**Example Code**

Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

**Notes and Warnings**

NA

------

- WiFiClass::encryptionType


**Description**

Return the Encryption Type associated with the network

**Syntax**

  uint8_t WiFiClass::encryptionType()

**Parameters**

The function requires no input parameter.

**Returns**

The function returns one unsigned integer value of wl_enc_type enum.

**Example Code**

Example: ConnectWithWPA

**Notes and Warnings**

NA

------

- WiFiClass::scanNetworks


**Description**

Start scan WiFi networks available

**Syntax**

  int8_t WiFiClass::scanNetworks()

**Parameters**

The function requires no input parameter.

**Returns**

The function returns the number of discovered networks as an integer.

**Example Code**

Example: ScanNetworks
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino)

**Notes and Warnings**

NA

-----

- WiFiClass::SSID


**Description**

Return the SSID discovered during the network scan

**Syntax**


  char* WiFiClass::SSID(uint8_t networkItem)

**Parameters**

networkItem: specify from which network item want to get the
information

**Returns**

The function returns ssid string of the specified item on the networks
scanned a list.

**Example Code**

Example: ScanNetworks

This example prints the Wifi shield’s MAC address, and scans fo
available Wifi networks using the Wifi shield. Every ten seconds, it
scans again. It doesn’t connect to any network, so no encryption
scheme is specified. The details of the code can be found in the
previous section of WiFiClass:: scanNetworks.

**Notes and Warnings**

NA

------

- WiFiClass::encryptionType


**Description**

Return the encryption type of the networks discovered during the
scanNetworks

**Syntax**



  uint8_t WiFiClass::encryptionType(uint8_t networkItem)

**Parameters**

networkItem : specify from which network item want to get the
information

**Returns**

encryption type (enum wl_enc_type) of the specified item on the
networks scanned a list

**Example Code**

Example: ScanNetworks

This example prints the Wifi shield’s MAC address, and scans for
available Wifi networks using the Wifi shield. Every ten seconds, it
scans again. It doesn’t connect to any network, so no encryption
scheme is specified. The details of the code can be found in the
previous section of WiFiClass:: scanNetworks.

**Notes and Warnings**

NA

-----

- WiFiClass::encryptionTypeEx


**Description**

Return the security type and encryption type of the networks
discovered during the scanNetworks

**Syntax**



  uint32_t WiFiClass::encryptionTypeEx(uint8_t networkItem)

**Parameters**

networkItem : specify from which network item want to get th
information

**Returns**

security and encryption type of the specified item on the networks
scanned a list

**Example Code**

Example: ScanNetworks

This example prints the Wifi shield’s MAC address, and scans for
available Wifi networks using the Wifi shield. Every ten seconds, it
scans again. It doesn’t connect to any network, so no encryption
scheme is specified. The details of the code can be found in the
previous section of WiFiClass:: scanNetworks.

**Notes and Warnings**

NA

-----

- WiFiClass::RSSI


**Description**

Return the RSSI of the networks discovered during the scanNetworks

**Syntax**



  int32_t WiFiClass::RSSI(uint8_t networkItem)

**Parameters**

networkItem : specify from which network item want to get the
information

**Returns**

signed value of RSSI of the specified item on the networks scanned a
list

**Example Code**

Example: ScanNetworks

This example prints the Wifi shield’s MAC address, and scans for
available Wifi networks using the Wifi shield. Every ten seconds, it
scans again. It doesn’t connect to any network, so no encryption
scheme is specified. The details of the code can be found in the
previous section of WiFiClass:: scanNetworks.

**Notes and Warnings**

NA

-----

- WiFiClass::status


**Description**

Return Connection status

**Syntax**



  uint8_t WiFiClass::status()

**Parameters**

The function requires no input parameter.

**Returns**

The function returns one of the values defined in wl_status_t as an
unsigned integer.

**Example Code**

Example: ConnectWithWPA

This example demos how to connect to an unencrypted WiFi network, and
prints the MAC address of the Wifi shield, the IP address obtained,
and other network details. The details of the code can be found in the
previous section of WiFiClass:: firmwareVersion.

**Notes and Warnings**

NA

----

- WiFiClass::hostByName

**Description**

Resolve the given hostname to an IP address

**Syntax**



  int WiFiClass::hostByName(const char* aHostname, IPAddress& aResult)

**Parameters**

aHostname : Name to be resolved

aResult : IPAddress structure to store the returned IP address

**Returns**

The function returns “1” if aIPAddrString was successfully converted
to an IP address,else otherwise, it will return as an error code.

**Example Code**

NA

**Notes and Warnings**

NA

-----

- WiFiClass::apbegin


**Description**

Start AP mode

**Syntax**



  int WiFiClass::apbegin(char* ssid, char* channel)

  int WiFiClass::apbegin(char* ssid, char* password, char* channel)

**Parameters**

ssid : SSID of the AP network

channel: AP’s channel, default 1

password : AP’s password

**Returns**

The function will return the WiFi status.

**Example Code**

Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

**Notes and Warnings**

NA

------

- WiFiClass::disablePowerSave

**Description**

Disable power-saving mode

**Syntax**

  int WiFiClass::disablePowerSave()

**Parameters**

The function requires no input parameter.

**Returns**

1 if disable success, 0 if faile

**Example Code**

NA

**Notes and Warnings**

NA
**Notes and Warnings**

NA
