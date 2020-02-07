public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
{
    var h = new ListNode(0);
    var l = h;

    var carry = 0;
    while (l1 != null || l2 != null || carry != 0)
    {
        var v = carry;
        if (l1 != null)
        {
            v += l1.val;
        }
        if (l2 != null)
        {
            v += l2.val;
        }
        carry = v / 10;
        var rem = v % 10;

        var newNode = new ListNode(rem);
        l.next = newNode;
        l = l.next;

        l1 = l1?.next;
        l2 = l2?.next;
    }

    return h.next;
}