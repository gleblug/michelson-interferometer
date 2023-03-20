#include <Stepper.h>

#define REVOL_STEPS 200
#define THREAD_PITCH 2.0 // in mm
#define SPEED 200

class Motor: public Stepper
{
public:
  Motor(int motor_pin_1, int motor_pin_2,
        int motor_pin_3, int motor_pin_4) : 
        Stepper(REVOL_STEPS, motor_pin_1, motor_pin_2,
                             motor_pin_3, motor_pin_4)
  {
    setSpeed(SPEED);
  }

  step_mm(double distance)
  {
    double steps = distance / THREAD_PITCH * REVOL_STEPS;
    step(static_cast<int>(steps));
  }
};

Motor motor1(8, 9, 10, 11);
Motor motor2(3, 4, 5, 6);

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("clockwise");
  for (int i = 0; i < 2000; ++i)
  {
    motor1.step(1);
    motor2.step(1);
  }
  delay(500);

  Serial.println("counterclockwise");
  for (int i = 0; i < 2000; ++i)
  {
    motor1.step(-1);
    motor2.step(-1);
  }
  delay(500);
}