abstract public class Gods{
  private String name;
  private String type;
  private int hitpoints;
  private int rank;
  private int worshipers;

  /**Constructor for god class*/
  public Gods(String name,String type, int hitpoints, int intinitialworshipers){

  }


  public String toString(){
    return ("Name: "+ name + "\nType:" + type + "\nHP: " + hitpoints + "Rank: " + rank + "Worshipers: " + worshipers)
  }


  /**Method that determines a Gods Rank based on worshipers;
  gets overridden because each God Type has different threshholds*/
  public abstract void determineRank(worshipers){

  }

  /**Method that gives God bonus based on Type and Rank;
  gets overridden because each God Type has bonusses*/
  public abstract void typeBonus(worshipers){

  }


}
