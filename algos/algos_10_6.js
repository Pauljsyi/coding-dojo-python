/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 *
 *
 */

function rotateStr(str, amnt) {
  for (let i = 0; i < amnt; i++) {
    let remainder = str.slice(0, -1);
    let lastChar = str.slice(str.length - 1);
    str = lastChar + remainder;
  }
  // console.log(str);
  return str;
}

// rotateStr(str, rotateAmnt1);
// rotateStr(str, rotateAmnt2);
// rotateStr(str, rotateAmnt3);
// rotateStr(str, rotateAmnt4);
// rotateStr(str, rotateAmnt5);
/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const two_strA1 = "ABCD";
const two_strB1 = "CDAB";
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const two_expected1 = true;

const two_strA2 = "ABCD";
const two_strB2 = "CDBA";
// Explanation: all same letters in 2nd string, but out of order
const two_expected2 = false;

const two_strA3 = "ABCD";
const two_strB3 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const two_expected3 = false;

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */
function isRotation(s1, s2) {
  let targetStr = s2;
  if (s1.length !== targetStr.length) {
    return false;
  }
  let currentStr = s1;
  for (let i = 0; i < s1.length; i++) {
    currentStr = rotateStr(currentStr, 1);
    // console.log("current String: ", currentStr);
    if (targetStr === currentStr) {
      return true;
    }
  }

  return false;
}

console.log("rotation1: ", isRotation(two_strA1, two_strB1));
console.log("rotation2: ", isRotation(two_strA2, two_strB2));
console.log("rotation3: ", isRotation(two_strA3, two_strB3));
