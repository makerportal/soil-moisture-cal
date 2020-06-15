// Simple Arduino code to predict volumetric
// water content in soil using a capacitive
// soil moisture sensor
//
int soil_pin = A0; // AOUT pin on sensor

float slope = 2.48; // slope from linear fit
float intercept = -0.71; // intercept from linear fit

void setup() {
  Serial.begin(9600); // serial port setup
  analogReference(EXTERNAL); // set the analog reference to 3.3V
}

void loop() {
  float voltage,vol_water_cont; // preallocate to approx. voltage and theta_v
  Serial.print("Voltage: ");
  voltage = (float(analogRead(soil_pin))/1023.0)*3.3;
  Serial.print(voltage); // read sensor
  Serial.print(" V, Theta_v: ");
  vol_water_cont = ((1.0/voltage)*slope)+intercept; // calc of theta_v (vol. water content)
  Serial.print(vol_water_cont);
  Serial.println(" cm^3/cm^3"); // cm^3/cm^3
  delay(100); // slight delay between readings
}
