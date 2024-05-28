const Thermostat = require('./thermostat.js')

const thermostat = new Thermostat()

// unit test for thermosat.js

describe('Thermostat Challenge - ', () => {
    it('When getTemperature is called, it should return a temp of 20', () => {
        expect(thermostat.getTemperature()).toBe(20);
    });
    it('When up() is called, it should increase temp by + 1', () => {
        expect(thermostat.up()).toBe(21);
    });
    it('When down() is called, it should decrease temp by - 1', () => {
        expect(thermostat.down()).toBe(20);
    });
    it('Test to determine powersave is set to "true", temp cannot go above 25', () => {
        expect(thermostat.powerSave).toBe(true)
        thermostat.powerSaveMode(true)
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        expect(thermostat.getTemperature()).toBe(25);
    });
    it('Test to determine powersave is set to "false", temp cannot go above 32', () => {
        expect(thermostat.powerSave).toBe(true)
        thermostat.powerSaveMode(false)
        expect(thermostat.powerSave).toBe(false)
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        thermostat.up()
        expect(thermostat.getTemperature()).toBe(32);
    });
    it('If reset() is called, it resets the current temp to the default temp (20)', () => {
        expect(thermostat.getTemperature()).toBe(32)
        thermostat.down()
        thermostat.down()
        expect(thermostat.getTemperature()).toBe(30)
        thermostat.reset()
        expect(thermostat.getTemperature()).toBe(20)
    })
})
