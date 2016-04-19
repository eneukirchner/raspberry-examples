var gpio = require("gpio");
var gpio4, intervalTimer;

console.log("Hallo");

// Flashing lights if LED connected to GPIO4
gpio4 = gpio.export(4, {
   ready: function() {
      intervalTimer = setInterval(function() {
         gpio4.set();
         setTimeout(function() { gpio4.reset(); }, 500);
      }, 1000);
   }
});

// reset the headers and unexport after 10 seconds
setTimeout(function() {
   clearInterval(intervalTimer);          // stops the voltage cycling

   gpio4.reset();
   gpio4.unexport(function() {
      // unexport takes a callback which gets fired as soon as unexporting is done
	
      console.log("Fertig");
      process.exit(); // exits your node program
   });
}, 10000)
