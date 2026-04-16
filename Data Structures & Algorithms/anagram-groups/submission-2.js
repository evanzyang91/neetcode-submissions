class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groups = {}
        for (let i = 0; i < strs.length; i++) {
            const sortedS = strs[i].split('').sort().join('');
            if (!groups[sortedS]) {
                groups[sortedS] = [];
            }
            groups[sortedS].push(strs[i]);
        }
        return Object.values(groups)
    }
}
