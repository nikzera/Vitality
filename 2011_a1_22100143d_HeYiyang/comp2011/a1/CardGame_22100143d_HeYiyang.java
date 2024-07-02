//Warning: Don't change this line.  If you change the package name, your code will not compile, and you will get zero points.
package comp2011.a1;

import java.util.Arrays;
import java.util.stream.Collectors;

/*
 * @author Yixin Cao (September 11, 2023)
 *
 * You have been deliver a hand of cards, and you sorted them in the suit-first order:
 * spades, hearts, clubs, and diamonds, each suit in decreasing order.
 *
 * See {@code main} where the input is in this order.
 * [♠89, ♠23, ♠14, ♠10, ♠8, ♠4, ♠2, ♥99, ♥18, ♥13, ♥11, ♥9, ♥8, ♥2, ♣77, ♣10, ♣4, ♦99, ♦89, ♦77, ♦14, ♦11, ♦9, ♦7, ♦6, ♦4]
 *
 * Your task is to reorder them into rank-first order: for cards of the same rank, you follow the order of spade, heart, club, and then diamond.
 *
 * For the given hand, the correct result should be:
 * [♥99, ♦99, ♠89, ♦89, ♣77, ♦77, ♠23, ♥18, ♠14, ♦14, ♥13, ♥11, ♦11, ♠10, ♣10, ♥9, ♦9, ♠8, ♥8, ♦7, ♦6, ♠4, ♣4, ♦4, ♠2, ♥2]
 *
 * You need to set your "text file encoding" to UTF-8 to run this class.
 * Otherwise, the suits of cards cannot be shown properly.
 *
 * The class {@code Card} is at the end of this file.
 */
public class CardGame_22100143d_HeYiyang { // Please change!

    /**
     * Warning:
     * You are reordering given cards, not creating new cards.
     * If you call "new Card()," your point will be zero.
     *
     * In the <code>main</code> method, the addresses of the input cards and final cards are printed.
     * They should be exactly the same.
     *
     * VERY IMPORTANT.
     *
     * I've discussed this question with the following students:
     *     1.
     *     2.
     *     3.
     *     ...
     *
     * I've sought help from the following Internet resources and books:
     *     1.COMP2011 LEC7 PPT
     *     2.
     *     3.
     *     ...
     *
     * Running time: O(nlogn).
     */
	
	static void mergeArrays (Card[] a1, Card[] a2, Card[] a) {
        int i1 = 0, i2 = 0, i = 0;
        while (i1 < a1.length && i2 < a2.length){
            if(a1[i1].getRank() >= a2[i2].getRank()){
                a[i++] = a1 [i1++];
            }
            else{
                a[i++] = a2 [i2++];
            }
        }
        while (i1 < a1.length){
            a[i++] = a1[i1++];
        }
        while (i2 < a2.length){
            a[i++] = a2[i2++];
        }
    }
	
    static void reorder(Card[] hand) {
    	if (hand.length <= 1) return ;
        int n = hand.length ;
        Card[] b = new Card[(n + 1) / 2];
        Card[] c = new Card[n / 2];
        for (int i = 0; i < (n + 1) / 2; i++){
            b[i] = hand[i];
        }
        for (int i = 0; i < n / 2; i++){
            c[i] = hand[(n + 1) / 2 + i];
        }
        reorder(b);
        reorder(c);
        mergeArrays(b, c, hand);
    }

    /*
     * The following is prepared for your reference.
     * You may freely revise it to test your code.
     */
    public static void main(String[] args) {
        byte[][] data = {{89, 23, 14, 10, 8, 4, 2}, // Spades
                {99, 18, 13, 11, 9, 8, 2}, // Hearts
                {77, 10, 4}, // Clubs
                {99, 89, 77, 14, 11, 9, 7, 6, 4} // Diamonds
        };

        int cardCount = Arrays.stream(data).mapToInt(p -> p.length).sum();
        Card[] hand = new Card[cardCount];
        int i = 0;
        for (byte suit = 0; suit < 4; suit++) {
            for (int j = 0; j < data[suit].length; j++)  {
                hand[i++] = new Card(suit, data[suit][j]);
            }
        }

        System.out.println("The original addresses of the input cards: " +
               Arrays.stream(hand)
               .map(p -> Integer.toHexString(System.identityHashCode(p)))
               .sorted()
                   .collect(Collectors.joining(", "))
       );

        System.out.println("original: " + Arrays.toString(hand));
        reorder(hand);
        System.out.println("after reordering: " + Arrays.toString(hand));

        // Make sure the following output is the same as the original one.
        System.out.println("The addresses of the cards after operations: " +
               Arrays.stream(hand)
               .map(p -> Integer.toHexString(System.identityHashCode(p)))
               .sorted()
                   .collect(Collectors.joining(", "))
       );
    }
}

/*
 * Each Card has a suit and an *unlimited* rank.
 */
class Card {
    /**
     *
     * No modification to the class {@code Card} is allowed.
     * If you change anything in this class, your work will not be graded.
     */
    private byte suit;
    private byte rank;
    public static final byte SPADE = 0;
    public static final byte HEART = 1;
    public static final byte CLUB = 2;
    public static final byte DIAMOND = 3;

    public Card(byte suit, byte rank) {
        this.suit = suit;
        this.rank = rank;
    }
    byte getSuit() {return suit;}
    byte getRank() {return rank;}

    public String toString() {
        String s = null;
        switch(suit) {
        case SPADE : s = "\u2660"; break;
        case HEART : s = "\u2665"; break;
        case CLUB : s = "\u2663"; break;
        case DIAMOND : s = "\u2666"; break;
        }
        s += String.valueOf(rank);
        return s;
    }
}
