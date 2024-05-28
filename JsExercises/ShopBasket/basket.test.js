const Basket = require('./basket')

const basket = new Basket

describe('Basket Class Unit/Mock Tests', () => {
    let doubleCandy = {
        name : 'Milkyway',
        price : 6
    }
    let doubleCandy2 = {
        name : 'Lindt',
        price: 9
    }

    it('If we call getTotalPrice, and the basket is empty, 0 should be returned', () => {
        expect(basket.getTotalPrice()).toBe(0);
    });
    it('If we call addItem() with a candy object, and then call getTotalPrice, we should see the updated price returned', () => {
        basket.addItem(doubleCandy)
        expect(basket.getTotalPrice()).toBe(6);
    });
    it('If i add multiple candy objects to the basket, and then call getTotalPrice, we should see the updated price returned', () => {
        basket.addItem(doubleCandy2)
        expect(basket.getTotalPrice()).toBe(15)
    })
})