# Soil Moisture Sensor Calibration with Arduino
Using the gravimetric method to calibrate a capacitive soil moisture sensor with an Arduino board.

Full tutorial at: https://makersportal.com/blog/2020/5/26/capacitive-soil-moisture-calibration-with-arduino

Soil moisture can be measured using a variety of different techniques: gravimetric, nuclear, electromagnetic, tensiometric, hygrometric, among others. The technique explored here uses a gravimetric technique to calibrate a capacitive-type electromagnetic soil moisture sensor. Capacitive soil moisture sensors exploit the dielectric contrast between water and soil, where dry soils have a relative permittivity between 2-6 and water has a value of roughly 80. Accurate measurement of soil water content is essential for applications in agronomy and botany - where the under- and over-watering of soil can result in ineffective or wasted resources. With water occupying up to 60% of certain soils by volume, depending on the specific porosity of the soil, calibration must be carried out in every environment to ensure accurate prediction of water content. Luckily, the accuracy of measurement devices has been increasing while the cost of the sensors have been decreasing. In this experiment, an Arduino board will be used to read the analog signal from the capacitive sensor, which will output voltage values which can be calibrated to volumetric soil moisture content via gravimetric methods (using volume and weight of dry and wet soil).

## Arduino Wiring

![Arduino + Sensor Wiring](https://images.squarespace-cdn.com/content/v1/59b037304c0dbfb092fbe894/1590622711213-VD9LBEVQMX3CFYBCR0GG/ke17ZwdGBToddI8pDm48kEoumxBTL0UGolEWVBoiqMV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0uN0nnuyYlMmBQSgz_9euuRumJ13WlPu-aG64ch8DNtSDGxITf5OzW_nhFmr2nsh1g/cap_soil_sensor_arduino_wiring.png?format=1500w)

## Experimental Setup

![Experimental Setup](https://images.squarespace-cdn.com/content/v1/59b037304c0dbfb092fbe894/1592252939525-1GZU487KCGYN09XG61N5/ke17ZwdGBToddI8pDm48kLkXF2pIyv_F2eUT9F60jBl7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0iyqMbMesKd95J-X4EagrgU9L3Sa3U8cogeb0tjXbfawd0urKshkc5MgdBeJmALQKw/capacitive_soil_moisture_experiment_setup.JPG?format=1500w)
