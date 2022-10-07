/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const three_str1 = "This is a test";
const three_expected1 = "test a is This";

const three_str2 = "hello";
const three_expected2 = "hello";

const three_str3 = "   This  is a   test  ";
const three_expected3 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(wordsStr) {
  let result = "";
  let temp = [];
  let tempVar = "";
  for (let i = 0; i < wordsStr.length; i++) {
    if (wordsStr[i] === " ") {
      let tempVar = "";
      for (let j = 0; j < wordsStr[i]; i++) {
        console.log();
      }
      // console.log(tempVar);
      console.log("index ", i);
      console.log("length ", wordsStr.length);
      // temp += wordsStr[i];
    }
    // console.log(tempVar);
  }
  // console.log(temp);
  // return result;
}

reverseWordOrder(three_str1);
// reverseWordOrder(three_expected2);
// reverseWordOrder(three_expected3);
