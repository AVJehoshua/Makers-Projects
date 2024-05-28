const candies = [
    { name: 'Aero', price: 1.99 },
    { name: 'Skitties', price: 2.99 },
    { name: 'Mars', price: 1.49 },
    { name: 'Maltesers', price: 3.49 },
    { name: 'Skittles', price: 1.49 },
    { name: 'Starburst', price: 5.99 },
    { name: 'Ricola', price: 1.99 },
    { name: 'Polkagris', price: 5.99 },
    { name: 'Pastila', price: 4.99 },
    { name: 'Mentos', price: 8.99 },
    { name: 'Raffaello', price: 7.99 },
    { name: 'Gummi bears', price: 10.99 },
    { name: 'Fraise Tagada', price: 5.99 }
    ];


    const searchCandies = (string, price) => {
        let filteredCandyNames = candies
            .filter((candy) => candy.name.match(new RegExp(string, 'i')) && candy.price <= price)
            .map((candy) => candy.name);
    
        return filteredCandyNames;
    };
    


// const searchCandies = (string, price) => {
//     let filteredCandy = candies.filter((candy) => {
//         const regex = new RegExp(string, 'i');
//         if ( regex.test(candy.name) && candy.price <= price ) {
//             return true;
//     }
//     return false;
// });
//     return filteredCandy
// }


console.log(searchCandies('Ma', 10))
console.log(searchCandies('Ma', 2))
console.log(searchCandies('S', 10))
// console.log(searchCandies('Ma', 10))

module.exports = searchCandies;


