package com.blockchain;
import java.util.ArrayList;


import com.google.gson.GsonBuilder;

public class Blockchain {
	
	public static ArrayList<Block> chain = new ArrayList<Block>();
	
	public static int difficulty = 5;
	

	
	public static Boolean isChainValid() {
		Block currentBlock; 
		Block previousBlock;
		String hashTarget = new String(new char[difficulty]).replace('\0', '0');
		
		//loop through blockchain to check hashes:
		for(int i=1; i < chain.size(); i++) {
			currentBlock = chain.get(i);
			previousBlock = chain.get(i-1);
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
	
	public static void addBlock(Block newBlock) {
		newBlock.mineBlock(difficulty);
		chain.add(newBlock);
	}
	
public static void displayChain() {
		
		for(int i=0; i<chain.size(); i++) {
			System.out.println("Block: " + i);
			System.out.println("Data: " + chain.get(i).getData());
			System.out.println("Timestamp: " + chain.get(i).getTimeStamp());
			System.out.println("PreviousHash: " + chain.get(i).getPreviousHash());
			System.out.println("Hash: " + chain.get(i).getHash());
			System.out.println("Nonce: " + chain.get(i).getNonce());
			System.out.println();
		}
		
	}
}