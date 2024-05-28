const Candy = require('./candy')

const candy = new Candy('Lindt', 6)

describe('Candy Class Unit Tests', () => {
    it('When i call getName(), we should see the name property returned', () => {
        expect(candy.getName()).toBe('Lindt');
    });
    it('When i call getPrice(), we should see the price property returned', () => {
        expect(candy.getPrice()).toBe(6);
    });
})