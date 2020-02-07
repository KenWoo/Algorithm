struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
    
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* h = new ListNode(0);
        auto l = h;

        int carry = 0;

        while (l1 != NULL || l2 != NULL || carry != 0)
        {
            int v = carry;
            if (l1 != NULL)
            {
                v += l1->val;
            }
            if (l2 != NULL)
            {
                v += l2->val;
            }

            carry = v / 10;
            int rem = v % 10;

            ListNode* newNode = new ListNode(rem);
            l->next = newNode;
            l = l->next;

            if (l1 != NULL)
            {
                l1 = l1->next;
            }
            if (l2 != NULL)
            {
                l2 = l2->next;
            }
        }

        return h->next;
    }
};