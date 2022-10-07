/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function makeFrequencyTable(arr) {
  // create an object
  // create a counter var
  // iterate through the array
  // push each iteration to the object
  // increment counter if repeated
  let result = {};

  for (let i = 0; i < arr.length; i++) {
    if (result[arr[i]]) {
      result[arr[i]] += 1;
    } else {
      result[arr[i]] = 1;
    }
  }
  console.log(result);
}
makeFrequencyTable(arr1);
makeFrequencyTable(arr2);
makeFrequencyTable(arr3);
/*****************************************************************************/

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const two_nums1 = [1];
const two_expected1 = 1;

const two_nums2 = [5, 4, 5];
const two_expected2 = 4;

const two_nums3 = [5, 4, 3, 4, 3, 4, 5];
const two_expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const two_nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const two_expected4 = 1;

function oddOccurrencesInArray(nums) {
  let result = {};

  for (let i = 0; i < nums.length; i++) {
    if (result[nums[i]]) {
      result[nums[i]] += 1;
      console.log("counter: ", result[nums[i]], "key", nums[i]);
    } else {
      result[nums[i]] = 1;
    }
  }
}

// console.log(oddOccurrencesInArray(two_nums1), "should equal", two_expected1);
// console.log(oddOccurrencesInArray(two_nums2), "should equal", two_expected2);
// console.log(oddOccurrencesInArray(two_nums3), "should equal", two_expected3);
// console.log(oddOccurrencesInArray(two_nums4), "should equal", two_expected4);
