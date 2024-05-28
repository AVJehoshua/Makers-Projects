
const squareNums = require('./filterMap.js')

const nums = [1, 2, 3, 4, 5]

describe("Map practice", () => {
    it('return squared array of num', () => {
        expect(squareNums(nums)).toStrictEqual([1, 4, 9, 16, 25]);
    });
})