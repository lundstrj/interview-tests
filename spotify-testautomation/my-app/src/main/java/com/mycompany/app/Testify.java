package com.mycompany.app;
import org.sikuli.script.*;

import com.sun.corba.se.impl.presentation.rmi.IDLTypeException;

import java.util.*;
import java.lang.*;
import java.net.IDN;

/**
 * @author Lundstromj
 * @version 0.1
 */
public class Testify
{

  private static String base_path = new String("C:/Users/LundstromJ/Dropbox/my-app/src/main/java/com/mycompany/app/");
  public Testify()
  {
	
  }
  
  public static void main(String[] args)
  {
	  System.out.println("Welcome to Testify");
	  smokeTest();
  }
  
  public static boolean eval(boolean got, boolean expected)
  {
	  return got == expected;
  }
  
  public static boolean smokeTest()
  {
	ArrayList<Boolean> results = new ArrayList<Boolean>();
	System.out.println("Launching smoke test...");
	results.add(eval(launch(), false));
	results.add(eval(login("lundstrj", "dasupercat", false), true));
	results.add(eval(login("no_user", "no_password", false), false));
	results.add(eval(search("Save Me, San Francisco"), true));
	results.add(eval(play("Save Me, San Francisco"), true));
	results.add(eval(searchAdvanced("Save Me, San Francisco"), true));
	return checkResults(results.toArray());
  }
  public static boolean checkResults(Object[] res)
  {
	boolean all_ok = true;
	for(int i = 0;i<res.length;i++)
	{
	  System.out.println("Test nbr: "+i+":"+res[i].toString());
	  if((boolean)res[i].equals(false))
	  {
	     all_ok = false;
	  }
	}
	if (all_ok)
	{
	  System.out.println("Smoke test: Passed");
	}
	else
	{
	  System.out.println("Smoke test: Failed");
	}
	return all_ok;
  }
  
  public static boolean launch()
  {
	System.out.println("launching spotify...");
    Screen s = new Screen();
    try
    {
    	s.click(base_path+"spotify_not_running.png", 0);
    }
    catch(FindFailed e)
    {
      e.printStackTrace();
      System.out.println("launch failed, unknown cause");
      return false;
    }
    // do things
    return true;
  }
  
  public static boolean login(String uname, String pwd, boolean remember_me)
  {
	System.out.println("loggin in...");
    Screen s = new Screen();
    try
    {
      boolean nothing_found = true;
      int counter = 0;
      boolean splash = false;
      boolean main_win = false;
      System.out.println("looking for splash or main window...");
      try
      {
    	System.out.println("start sleeping");
    	Thread.currentThread();
		Thread.sleep(2000);
		System.out.println("done sleeping");
      }
      catch(InterruptedException ie)
      {
    	  System.out.println("failed while sleeping");
      }
      while (nothing_found && (counter < 100))
      {
    	 counter++;
    	 System.out.println(s.exists(base_path+"small_splash.png").toString());
    	 try
    	 {
    	   int a = (int) s.exists(base_path+"small_splash.png").getScore();
    	   System.out.println(a);
    	   splash = !s.exists(base_path+"small_splash.png").toString().equals(null);
    	   main_win = s.exists(base_path+"spotify_main_loaded.png").toString().equals(null);
    	 }
    	 catch (Exception ie)
    	 {
    		 System.out.println("woups");
    	 }
    	 if (splash || main_win)
    	 {
    		 System.out.println("found something");
    		 nothing_found = false;
    	 }
      }
      if (nothing_found)
      {
    	  System.out.println("loggin timed out.");	  
    	  return false;
      }
      if (main_win)
      {
    	  System.out.println("login success (remembered)");
          return true;  
      }
      else
      {
        s.click(base_path+"uname_field.png");
        s.type(null, uname+"\t", 0);
        s.type(null, pwd+"\t", 0);
        if (remember_me)
        {
        	s.click(base_path+"remember_me.png");
        }
        s.click(base_path+"login.png", 0);
        try
        {
      	  System.out.println("start sleeping");
      	  Thread.currentThread();
  		  Thread.sleep(2000);
  		  System.out.println("done sleeping");
        }
        catch(InterruptedException ie)
        {
      	  System.out.println("failed while sleeping");
        }
        if((int)s.exists(base_path+"spotify_main_loaded.png").getScore() == 0)
        {
          System.out.println("login success (dialog)");
          return true;	
        }
        else
        {
          System.out.println("login failed at dialog!");
          return false;
        }
        
      }
    }
    catch(FindFailed e)
    {
      e.printStackTrace();
      System.out.println("login failed, unknown cause");
      return false;
    }
  }
  public static boolean playRandomSong()
  {
	System.out.println("playRandomSong not implemented yet");
    return false;
  }
  public static boolean play(String song)
  {
	System.out.println("play not implemented yet");
    return false;
  }
  
  public static boolean search(String pattern)
  {
	  System.out.println("search not implemented yet");
	  return false;
  }
  public static boolean searchAdvanced(String pattern)
  {
	  System.out.println("searchAdvanced not implemented yet");
	  return false;
  }
}

