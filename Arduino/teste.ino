
#include <FastLED.h>

#define LED_PIN     8
#define NUM_LEDS    140
#define BRIGHTNESS  50
#define LED_TYPE    WS2811
#define COLOR_ORDER GRB
CRGB leds[NUM_LEDS];

int var[10];

 

void setup() {
    Serial.begin(9600);
    FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
    FastLED.setBrightness(  BRIGHTNESS );

    
    
    while(!Serial){
      
    }
   
}



void loop() {
    
    fill_solid(leds, NUM_LEDS, CRGB(0,0,0));
    
    
    if(Serial.available()==6 && Serial.read()==15){
      
      for(int k=0;k<5;k++){
        var[k]=Serial.read();
     }

//Designed for specific hardware,build according to yours. //Unfolded for clarity

      for(int i=0;i<var[0];i++){
        leds[i]=CRGB(10*i,50/i,50/i);
      }

      for(int i=26;i>26-var[1] ;i--){
        leds[i]=CRGB(255/(i-14),2*(i-14),2*(i-14));
      }

      for(int i=27;i<var[2]+27;i++){
        leds[i]=CRGB(10*(i-27),50/(i-27),50/(i-27));
      }

      for(int i=54;i>54-var[3];i--){
        leds[i]=CRGB(255/(i-41),2*(i-41),2*(i-41));
      }

      for(int i=55;i<var[4]+55;i++){
        leds[i]=CRGB(10*(i-55),50/(i-55),50/(i-55));
      }
     FastLED.show();
     
    
   }
   
}
  

 
