const searchCandies = require('./candySearch.js')

describe("Search Candies Challenge", () => {
    it('When we call searchCandies(), with a string - "Ma" and price of 10, we can see a list of relevant candies', () => {
        expect(searchCandies('Ma', 10)).toEqual(['Mars', 'Maltesers']);
    });
    it('With a string of "Ma" and a price of 2', () => {
        expect(searchCandies('Ma', 2)).toEqual(['Mars']);
    });
    it('With a string of "S" and a price of 10', () => {
        expect(searchCandies('S', 10)).toEqual(['Skitties', 'Skittles', 'Starburst']);
    });
})