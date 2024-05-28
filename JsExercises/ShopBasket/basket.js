const Candy = require("./candy")

candy = new Candy('Mars', 4.99)

class Basket{ 
    constructor() {
        this.shop_basket = [{
            name : " ",
            price : 0
        }]
    }

    getTotalPrice() {
        let totalPrice = 0
        for (let i = 0; i < this.shop_basket.length; i++) {
            totalPrice += this.shop_basket[i].price
        }
        return totalPrice
    }

    addItem(candy) {
        this.shop_basket.push(candy)
    }
}


basket = new Basket
console.log(basket.getTotalPrice())
console.log(basket.addItem(candy))
console.log(basket.getTotalPrice())


module.exports = Basket