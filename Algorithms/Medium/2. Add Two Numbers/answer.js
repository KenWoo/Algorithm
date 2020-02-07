/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var h = l = new ListNode(0);
    var carry = 0;
    while(l1 || l2 || carry) {
        var v = carry;
        if (l1) v += l1.val;
        if (l2) v += l2.val;
        carry = parseInt(v / 10);
        var rem = v % 10;
        var newNode = new ListNode(rem);
        l.next = newNode;
        l = l.next;
        
        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }
    return h.next;
};