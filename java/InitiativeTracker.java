/*  Ideas


*/
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Scanner;
import java.util.Random;
import java.io.*;

public class InitiativeTracker {
  public static void main(String[] args) throws FileNotFoundException {
/*
    JFrame frame = new JFrame();
    frame.setSize(600, 850);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Container container = frame.getContentPane();
    container.setLayout(new FlowLayout());

    JTextField textField = new JTextField();
    textField.setPreferredSize(new Dimension(150, 25));

    JLabel label = new JLabel("Number of Enemies:");

    JButton okButton = new JButton("OK");
    okButton.addActionListener(new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent e) {
        String input = textField.getText();
        System.out.println("Number of Enemies: " + input);
        label.setText(input);
      }
    });
    container.add(textField);
    container.add(okButton);
    container.add(label);

    frame.setVisible(true);
*/
    // GET NUMBER OF ENEMIES
    System.out.print("Number of enemies: ");
    Scanner numEnemies = new Scanner(System.in);
    int addEnemyLoops = numEnemies.nextInt();

    // GET NUMBER OF ALLIES
    System.out.print("Number of allies: ");
    Scanner numAllies = new Scanner(System.in);
    int addAllyloops = numAllies.nextInt();

    // MAKE ARRAY OF APPROPRIATE SIZE
    int arrSize = addAllyloops + addEnemyLoops;
    Character[] charArray = new Character[arrSize];

    // INSERT ENEMIES INTO ARRAY
    for(int i = 0; i < addEnemyLoops; i++) {
      Character newEnemy = addEnemy();
      charArray[i] = newEnemy;
    }

    // INSERT ALLIES INTO ARRAY
    for(int i = addEnemyLoops; i < arrSize; i++) {
      Character newAlly = addAlly();
      charArray[i] = newAlly;
    }

    // SORT ARRAY
    Character[] sortedArray = sortArray(charArray);

    // PRINT ARRAY TO CONSOLE
/*
    System.out.println("****** ORDER OF PLAY ******");
    for(int i = 0; i < arrSize; i++) {
      printArray(sortedArray[i]);
    }
*/
    // PRINT ARRAY TO FILE
    PrintStream file = new PrintStream(new File ("Encounter.txt"));
    file.println("****** ORDER OF PLAY ******");
    for(int i = 0; i < arrSize; i++) {
      file.println(sortedArray[i].name + ", " + sortedArray[i].initiative);
    }
  }

  public static Character[] sortArray(Character[] unsortedArray) {
    Character temp;
    for(int i = 1; i < unsortedArray.length; i++) {
        temp = unsortedArray[i];
        int j = i;
        while (j > 0 && unsortedArray[j-1].initiative < temp.initiative) {
            unsortedArray[j] = unsortedArray[j-1];
            j--;
        }
        unsortedArray[j] = temp;
    }
    return unsortedArray;
  }

  public static Character addEnemy() {
    Character newEnemy = new Character();
    Random randomInit = new Random();
    System.out.print("Enemy Name: ");
    Scanner enemyName = new Scanner(System.in);
    newEnemy.name = enemyName.nextLine();
    System.out.print("Dexterity bonus: ");
    Scanner enemyDexBonus = new Scanner(System.in);
    int dexBonus = enemyDexBonus.nextInt();
    newEnemy.initiative = (randomInit.nextInt(20)+1)+dexBonus;
    return newEnemy;
  }

  public static Character addAlly(){
      Character newAlly = new Character();
      System.out.print("Ally Name: ");
      Scanner allyName = new Scanner(System.in);
      newAlly.name = allyName.nextLine();
      System.out.print("Initiative: ");
      Scanner allyInit = new Scanner(System.in);
      newAlly.initiative = allyInit.nextInt();
      return newAlly;
  }

  public static void printArray(Character guyToPrint) {
    System.out.println(guyToPrint.name + ", " + guyToPrint.initiative);
  }
}



class Character {
  public String name;
  public int initiative;
  public int dexBonus;

  public Character() {
    this.name = "noname";
    this.initiative = -1;
    this.dexBonus = 0;
  }

  public Character(String name, int initiative) {
    this.name = name;
    this.initiative = initiative;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setInitiative(int initiative) {
    this.initiative = initiative;
  }

}
