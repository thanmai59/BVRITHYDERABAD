package action;
import java.util.ArrayList;
import com.google.gson.GsonBuilder;

public class NoobChain {
	
	public static ArrayList<blockchain> blockc = new ArrayList<blockchain>();
	public static int difficulty = 5;

	public static void main(String[] args) {	
		//add our blocks to the blockchain ArrayList:
		
		System.out.println("Trying to Mine block 1... ");
		addBlock(new blockchain("Hi im the first block", "0"));
		
		System.out.println("Trying to Mine block 2... ");
		addBlock(new blockchain("Yo im the second block",blockc.get(blockc.size()-1).hash));
		
		System.out.println("Trying to Mine block 3... ");
		addBlock(new blockchain("Hey im the third block",blockc.get(blockc.size()-1).hash));	
		
		System.out.println("\nBlockchain is Valid: " + isChainValid());
		
		String blockchainJson = StringUtil.getJson(blockc);
		System.out.println("\nThe block chain: ");
		System.out.println(blockchainJson);
	}
	
	public static Boolean isChainValid() {
		blockchain currentBlock; 
		blockchain previousBlock;
		String hashTarget = new String(new char[difficulty]).replace('\0', '0');
		
		//loop through blockchain to check hashes:
		for(int i=1; i < blockc.size(); i++) {
			currentBlock = blockc.get(i);
			previousBlock = blockc.get(i-1);
			//compare registered hash and calculated hash:
			if(!currentBlock.hash.equals(currentBlock.calculateHash()) ){
				System.out.println("Current Hashes not equal");			
				return false;
			}
			//compare previous hash and registered previous hash
			if(!previousBlock.hash.equals(currentBlock.previousHash) ) {
				System.out.println("Previous Hashes not equal");
				return false;
			}
			//check if hash is solved
			if(!currentBlock.hash.substring( 0, difficulty).equals(hashTarget)) {
				System.out.println("This block hasn't been mined");
				return false;
			}
			
		}
		return true;
	}
	
	public static void displaychain() {
		for(int i=0; i<blockc.size(); i++) {
		System.out.println("Block: " + i);
		System.out.println("Data: " + blockc.get(i).getData());
		System.out.println("Timestamp: " +
		blockc.get(i).getTimeStamp());
		System.out.println("PreviousHash: " +
		blockc.get(i).getPreviousHash());
		System.out.println("Hash: " + blockc.get(i).getHash());
		System.out.println("Nonce: " + blockc.get(i).getNonce());
		System.out.println();
		}
	}
	
	public static void addBlock(blockchain newBlock) {
		newBlock.mineBlock(difficulty);
		blockc.add(newBlock);
	}
	
	
}