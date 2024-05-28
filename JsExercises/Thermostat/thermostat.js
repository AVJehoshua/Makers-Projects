class Thermostat {
    constructor() {
        this.powerSave = true
        this.temperature = 20
        this.maxTemp = 25
        this.maxTemp2 = 32
        this.minTemp = 10
    }
    
    getTemperature() {
        return this.temperature
    }

    up() {
        if (this.powerSave == true && this.temperature == this.maxTemp) {
            return this.maxTemp
        }
        else if (this.powerSave == false && this.temperature == this.maxTemp2) {
            return this.maxTemp2
        } 
        return this.temperature += 1
    }
    
    down() {
        if (this.temperature == this.minTemp) {
            this.temperature = 10
            return 'Temp cannot go below 10 degrees!'
        } else
        return this.temperature -= 1
    }

    powerSaveMode(bool) {
        this.powerSave = bool

        if ( this.powerSave == false ) {
            if ( this.temperature == this.maxTemp2 ) {
                return 'Cannot go higher, powersave is off!'
            }
        }
        
        else 
            ( this.powerSave == true ) 
                if ( this.temperature == this.maxTemp ) {
                    return 'Cannot go higher, powersave is on'
                }
            }


        reset() {
            return this.temperature = 20
        }
    }


// const thermostat = new Thermostat();

// console.log(thermostat.getTemperature()); // should return 20

// console.log(thermostat.up());
// console.log(thermostat.up());
// console.log(thermostat.getTemperature()); // should now return 22

// console.log(thermostat.down());
// console.log(thermostat.getTemperature()); // should now return 21

// console.log(thermostat.powerSaveMode(true)); // PSM is now on, max temperature is 25

// for (let i = 0 ; i < 10 ; i++) {
//     console.log(thermostat.up());
// }

// console.log(thermostat.getTemperature());  // should be 25 (max reached)

// console.log(thermostat.powerSaveMode(false)); // PSM is now off, max temperature is no more 25

// console.log(thermostat.up());
// console.log(thermostat.getTemperature());  // should now return 26

// for (let i = 0 ; i < 9 ; i++) {
//     console.log(thermostat.up());
// }

// console.log(thermostat.getTemperature());  // should now return 32


// console.log(thermostat.reset());
// console.log(thermostat.getTemperature());  // should be back to 20


module.exports = Thermostat;