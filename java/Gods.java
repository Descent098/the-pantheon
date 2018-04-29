abstract public class Gods{
  private String name;
  private String type;
  private int hitpoints;
  private int rank;
  private int worshipers;

  /**Constructor for god class*/
  public Gods(String initialName,String initialType, int initialHitPoints, int initialWorshipers){
    name = initialName;
    type = initialType;
    hitpoints = initialHitPoints;
    worshipers = initialWorshipers;
  }


  public int getWorshipers(){
    int newWorshipers = new Integer(worshipers);
    return newWorshipers;
  }

  public void setRank(int newRank){
    rank = newRank;
  }

  public String toString(){
    return ("Name: "+ name + "\nType:" + type + "\nHP: " + hitpoints + "\nRank: " + rank + "\nWorshipers: " + worshipers);
  }


  /**Method that determines a Gods Rank based on worshipers;
  gets overridden because each God Type has different threshholds*/
  public abstract void determineRank();

  /**Method that gives God bonus based on Type and Rank;
  gets overridden because each God Type has bonusses*/
  public abstract void typeBonus(int worshipers);


}
