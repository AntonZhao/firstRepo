import java.util.List;
import java.util.Random;
import java.lang.Math;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}


public class addTwoNumber {
    public static void main(String[] args) {
        ListNode dummyHead1 = new ListNode(0);
        ListNode dummyHead2 = new ListNode(0);

        ListNode l1 = dummyHead1,l2 = dummyHead2;

        int max=10,min=1;
        for (int i =0;i<3;i++){
            l1.next = new ListNode((int) (Math.random()*(max-min)+min));
            l2.next = new ListNode((int) (Math.random()*(max-min)+min));
            if (i<2){
                l1 = l1.next;
                l2 = l2.next;
            }
        }

        show(dummyHead1);
        show(dummyHead2);
        ListNode res = add(dummyHead1,dummyHead2);
        show(res);
        
    }

    public static void show(ListNode L){
        while (L != null){
            System.out.print(L.val+"-");
            if (L!=null)  L=L.next;
        }
        System.out.println();
    }
    public static ListNode add(ListNode l1,ListNode l2){
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q=l2, current = dummyHead;
        int carry = 0;
        while(p != null || q != null){
            int x = (p!=null) ? p.val : 0;
            int y = (q!=null) ? q.val : 0;
            int sum = x + y +carry;
            carry = sum/10;
            current.next = new ListNode(sum%10);
            current = current.next;
            if(p!=null) p=p.next;
            if(q!=null) q=q.next;
        }
        if(carry>0)
            current.next = new ListNode(carry);

        return dummyHead.next;
    }
}
