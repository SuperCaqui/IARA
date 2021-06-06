/* IRremoteESP8266: IRsendDemo - demonstrates sending IR codes with IRsend.
 *
 * Version 1.1 January, 2019
 * Based on Ken Shirriff's IrsendDemo Version 0.1 July, 2009,
 * Copyright 2009 Ken Shirriff, http://arcfn.com
 *
 * An IR LED circuit *MUST* be connected to the ESP8266 on a pin
 * as specified by kIrLed below.
 *
 * TL;DR: The IR LED needs to be driven by a transistor for a good result.
 *
 * Suggested circuit:
 *     https://github.com/crankyoldgit/IRremoteESP8266/wiki#ir-sending
 *
 * Common mistakes & tips:
 *   * Don't just connect the IR LED directly to the pin, it won't
 *     have enough current to drive the IR LED effectively.
 *   * Make sure you have the IR LED polarity correct.
 *     See: https://learn.sparkfun.com/tutorials/polarity/diode-and-led-polarity
 *   * Typical digital camera/phones can be used to see if the IR LED is flashed.
 *     Replace the IR LED with a normal LED if you don't have a digital camera
 *     when debugging.
 *   * Avoid using the following pins unless you really know what you are doing:
 *     * Pin 0/D3: Can interfere with the boot/program mode & support circuits.
 *     * Pin 1/TX/TXD0: Any serial transmissions from the ESP8266 will interfere.
 *     * Pin 3/RX/RXD0: Any serial transmissions to the ESP8266 will interfere.
 *   * ESP-01 modules are tricky. We suggest you use a module with more GPIOs
 *     for your first time. e.g. ESP-12 etc.
 */

#include <Arduino.h>
#include <IRremoteESP8266.h>
#include <IRsend.h>

const uint16_t kIrLed = 4;  // ESP8266 GPIO pin to use. Recommended: 4 (D2).

IRsend irsend(kIrLed);  // Set the GPIO to be used to sending the message.

// Example of data captured by IRrecvDumpV2.ino
/*
uint16_t rawData[67] = {9000, 4500, 650, 550, 650, 1650, 600, 550, 650, 550,
                        600, 1650, 650, 550, 600, 1650, 650, 1650, 650, 1650,
                        600, 550, 650, 1650, 650, 1650, 650, 550, 600, 1650,
                        650, 1650, 650, 550, 650, 550, 650, 1650, 650, 550,
                        650, 550, 650, 550, 600, 550, 650, 550, 650, 550,
                        650, 1650, 600, 550, 650, 1650, 650, 1650, 650, 1650,
                        650, 1650, 650, 1650, 650, 1650, 600};
// Example Samsung A/C state captured from IRrecvDumpV2.ino
*/
uint8_t samsungState[kSamsungAcStateLength] = {
    0x02, 0x92, 0x0F, 0x00, 0x00, 0x00, 0xF0,
    0x01, 0xE2, 0xFE, 0x71, 0x40, 0x11, 0xF0};

uint16_t rawData[347] = {9070, 4508,  560, 562,  612, 530,  582, 536,  562, 1696,  582, 1674,  588, 538,  558, 562,  560, 562,  560, 564,  558, 566,  558, 562,  586, 536,  562, 562,  610, 530,  562, 564,  582, 1674,  560, 564,  582, 564,  560, 540,  560, 586,  560, 564,  536, 562,  584, 564,  560, 538,  586, 538,  586, 552,  586, 538,  584, 540,  560, 564,  558, 564,  584, 562,  560, 564,  536, 1698,  558, 566,  558, 564,  560, 562,  582, 542,  586, 1712,  556, 564,  562, 538,  584, 538,  560, 562,  584, 538,  560, 562,  584, 564,  560, 538,  584, 540,  558, 562,  586, 1670,  586, 580,  546, 552,  560, 1696,  584, 1674,  560, 1696,  582, 540,  584, 1670,  562, 13566,  9072, 4532,  562, 564,  584, 538,  584, 540,  584, 1672,  584, 1672,  586, 564,  534, 562,  560, 562,  584, 538,  584, 540,  608, 556,  558, 540,  584, 540,  584, 538,  584, 540,  582, 1670,  562, 564,  584, 538,  582, 540,  582, 542,  582, 538,  586, 536,  612, 532,  582, 538,  584, 540,  584, 540,  582, 538,  586, 538,  584, 538,  586, 538,  582, 542,  582, 542,  584, 1670,  584, 538,  612, 530,  582, 538,  584, 564,  536, 1696,  584, 540,  558, 564,  582, 540,  584, 562,  558, 540,  582, 540,  558, 564,  584, 538,  610, 532,  584, 562,  560, 1672,  584, 562,  560, 540,  582, 1676,  584, 1674,  582, 1674,  584, 540,  582, 1676,  608, 13510,  9068, 4508,  584, 540,  608, 534,  584, 538,  584, 1670,  586, 1674,  582, 540,  582, 540,  584, 538,  584, 538,  584, 540,  584, 562,  558, 540,  584, 540,  610, 530,  572, 552,  582, 1676,  582, 538,  586, 540,  558, 564,  582, 540,  558, 564,  582, 564,  558, 538,  584, 540,  582, 540,  610, 530,  560, 564,  582, 540,  584, 540,  582, 540,  560, 564,  582, 542,  580, 1674,  584, 540,  582, 540,  582, 540,  560, 564,  586, 1688,  584, 540,  582, 540,  584, 540,  584, 542,  580, 540,  584, 540,  558, 564,  582, 540,  582, 540,  582, 540,  582, 1676,  606, 534,  582, 538,  584, 1672,  582, 1676,  584, 1672,  584, 540,  582, 1674,  582};  // UNKNOWN 27C6CE79

uint16_t rawData2[347] = {9074, 4532,  560, 560,  562, 562,  560, 562,  562, 1696,  560, 1696,  560, 560,  562, 562,  560, 562,  562, 562,  562, 560,  588, 554,  562, 562,  560, 562,  562, 560,  560, 562,  562, 560,  564, 560,  562, 562,  560, 560,  564, 560,  562, 562,  560, 562,  612, 528,  562, 560,  562, 562,  562, 560,  562, 560,  562, 560,  586, 538,  586, 536,  562, 560,  562, 564,  582, 1674,  558, 562,  588, 554,  558, 562,  562, 560,  562, 1698,  558, 562,  562, 560,  562, 562,  560, 562,  562, 562,  562, 560,  562, 562,  560, 560,  588, 552,  562, 560,  562, 1696,  560, 562,  566, 556,  562, 1696,  560, 1696,  560, 1698,  560, 562,  560, 562,  588, 13558,  9046, 4532,  560, 562,  588, 554,  584, 538,  560, 1698,  560, 1696,  562, 560,  562, 562,  560, 562,  560, 562,  584, 538,  562, 560,  564, 560,  562, 560,  588, 552,  584, 536,  588, 536,  586, 538,  562, 560,  562, 562,  562, 562,  560, 560,  562, 562,  562, 560,  562, 560,  562, 560,  588, 554,  560, 560,  586, 538,  584, 536,  562, 560,  564, 560,  562, 560,  588, 1672,  560, 562,  560, 562,  584, 538,  562, 560,  588, 1688,  560, 560,  586, 538,  560, 562,  560, 560,  562, 560,  564, 562,  562, 562,  584, 536,  562, 562,  560, 562,  586, 1672,  610, 528,  562, 560,  586, 1674,  558, 1696,  562, 1696,  560, 560,  560, 560,  562, 13542,  9072, 4534,  582, 538,  560, 560,  566, 558,  586, 1672,  560, 1696,  560, 562,  560, 562,  586, 538,  562, 560,  586, 538,  588, 552,  588, 536,  584, 536,  584, 538,  564, 560,  586, 536,  562, 562,  562, 560,  562, 560,  584, 538,  560, 562,  586, 538,  612, 530,  560, 562,  560, 562,  562, 560,  560, 562,  586, 538,  560, 562,  562, 560,  562, 562,  560, 562,  584, 1672,  562, 560,  588, 552,  562, 562,  584, 536,  586, 1674,  558, 562,  562, 560,  562, 562,  562, 562,  560, 562,  586, 536,  562, 562,  560, 562,  588, 554,  586, 536,  586, 1672,  560, 562,  584, 538,  586, 1672,  584, 1674,  584, 1672,  584, 538,  560, 560,  612};  // UNKNOWN 7968E20A


void setup() {
  irsend.begin();
#if ESP8266
  Serial.begin(115200, SERIAL_8N1, SERIAL_TX_ONLY);
#else  // ESP8266
  Serial.begin(115200, SERIAL_8N1);
#endif  // ESP8266
}

void loop() {
  //Serial.println("NEC");
  //irsend.sendNEC(0x00FFE01FUL);
  //delay(2000);
  //Serial.println("Sony");
  //irsend.sendSony(0xa90, 12, 2);  // 12 bits & 2 repeats
  //delay(2000);
  Serial.println("liga");
  irsend.sendRaw(rawData, 347, 20);  // Send a raw data capture at 38kHz.
  delay(2000);
  Serial.println("desliga");
  irsend.sendRaw(rawData2, 347, 20);  // Send a raw data capture at 38kHz.
  
  //Serial.println("a Samsung A/C state from IRrecvDumpV2");
  //irsend.sendSamsungAC(samsungState);
  delay(2000);
}
