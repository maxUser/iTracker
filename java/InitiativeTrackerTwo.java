/*  This version of InitiativeTracker allows the user to input enemies in groups as opposed to
/*  individually if some are of the same type (i.e. 5 goblins). This version automatically assigns
/*  numbers to enemies within the same group.
/*  OUTPUT: prints onto a file named encounter.txt the initiative order.
*/
import java.util.Scanner;
import java.util.Random;
import java.io.*;

public class InitiativeTrackerTwo {
  public static void main(String[] args) throws FileNotFoundException {
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

    /* ADD MULTIPLE ENEMIES */
    if(addEnemyLoops > 0) {
      int numOfCurrEnemies = 0;
      do {
        charArray = addMultipleSameEnemy(charArray, numOfCurrEnemies);
        numOfCurrEnemies += charArray[numOfCurrEnemies].trackingNum;
      } while(numOfCurrEnemies < addEnemyLoops);
    }
/*
    // INSERT ENEMIES INTO ARRAY INDIVIDUALLY
    for(int i = 0; i < addEnemyLoops; i++) {
      Character newEnemy = addEnemy();
      charArray[i] = newEnemy;
    }
*/
    // INSERT ALLIES INTO ARRAY INDIVIDUALLY
    for(int i = addEnemyLoops; i < arrSize; i++) {
      Character newAlly = addAlly();
      charArray[i] = newAlly;
    }

    // SORT ARRAY
    Character[] sortedArray = sortArray(charArray);

    // PRINT ARRAY TO CONSOLE
    System.out.println("****** ORDER OF PLAY ******");
    for(int i = 0; i < arrSize; i++) {
      printArray(sortedArray[i]);
    }

    // PRINT ARRAY TO FILE
    PrintStream file = new PrintStream(new File ("Encounter.txt"));
    file.println("****** ORDER OF PLAY ******");
    for(int i = 0; i < arrSize; i++) {
      file.println(sortedArray[i].name + ", " + sortedArray[i].initiative);
    }
  }

  public static Character[] addMultipleSameEnemy(Character[] charArray, int numOfCurrEnemies) {
    Random randomInit = new Random();
    System.out.println("=================");
    System.out.print("Enemy name: ");
    Scanner getEnemyName = new Scanner(System.in);
    String enemyName = getEnemyName.nextLine();
    System.out.print("Dexterity bonus: ");
    Scanner enemyDexBonus = new Scanner(System.in);
    int dexBonus = enemyDexBonus.nextInt();
    System.out.print("Number of " + enemyName + "s: ");
    Scanner getNumOfEnemy = new Scanner(System.in);
    int counter = getNumOfEnemy.nextInt();

    // ADD TO ARRAY
    for(int i = 0; i < counter; i++) {
      Character newEnemy = new Character();
      if(counter == 1) {
        newEnemy.name = enemyName;
      } else {
        newEnemy.name = enemyName + (i+1);
      }
      newEnemy.initiative = (randomInit.nextInt(20)+1)+dexBonus;
      newEnemy.trackingNum = counter;
      charArray[numOfCurrEnemies] = newEnemy;
      numOfCurrEnemies++;
    }
    return charArray;
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
      System.out.println("=================");
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
  public int trackingNum;

  public Character() {
    this.name = "noname";
    this.initiative = -1;
    this.dexBonus = 0;
    this.trackingNum = -1;
  }

  public Character(String name, int initiative) {
    this.name = name;
    this.initiative = initiative;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setTrackingNum(int trackingNum) {
    this.trackingNum = trackingNum;
  }

  public void setInitiative(int initiative) {
    this.initiative = initiative;
  }

}
