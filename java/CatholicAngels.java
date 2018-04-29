

public class CatholicAngels extends Gods{

  public CatholicAngels(String initialName,String initialType, int initialHitPoints, int initialWorshipers){
    super(initialName,initialType,initialHitPoints,initialWorshipers);
    determineRank();

  }

  /**Method that determines a Gods Rank based on worshipers;
  gets overridden because each God Type has different threshholds*/
  public void determineRank(){
    int currentWorshipers = getWorshipers();

		if (getWorshipers()>= 1000000){
			setRank(1);
    }

		else if(getWorshipers()>= 750000){
			setRank(2);
    }

		else if(getWorshipers()>= 500000){
			setRank(3);
    }

		else if(getWorshipers() >= 250000){
			setRank(4);
    }
		else{
      setRank(5);
    }

  }

  /**Method that gives God bonus based on Type and Rank;
  gets overridden because each God Type has bonusses*/
  public void typeBonus(int worshipers){

  }
}
