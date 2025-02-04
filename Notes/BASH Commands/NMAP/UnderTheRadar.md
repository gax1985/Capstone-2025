
The CIDR , we send one test , one port , one machine, and if we are looking for multiple ports in a single machine, we need a wait time to scan the next port. 
How long? if the target does not have exceptional monitoring (not monitoring for specific ports), this is less of an issue. But, we have to think how infrequent we would touch that machine before being detected as aport scanner ( once every 24 hours), but we want to avoid the possibility of showing up in a historical log. If someone is trying to find out when you got in, you can space the scans to weeks. Ultra low frequency means months. We are trying to make part of the scan disappear in the rollover log. If they are using a Circular Buffer to rotate the log, you need to let it rotate once before the next scan. If we know the target uses circular buffer every two weeks, you make it two weeks plus one day. Sometimes they only go and check the last archive log. If you can get past their rollover, you can disappear into the part. 
Ron would write the code to do it himself rather than using nmap. 


max rate 1 max-retries 1 

The previous example was detected because the scanning person would do the scan from hotel to hotel. Ron detected him because he had taps in place in the hotel, and he accidently picked up this guy.
Ron gained insight of behaviour he has not seen before. By putthing the algorithms in place, and writing them youself, you can think of patterns you would look for . 

You ask yourself : how would I go around it? 
and then again : how would I detect these steps?

Interesting Assignment : write code that exist in RAM, and the code makes the process jump from one place to another in RAM. you would have two programs, one written by you and one by your 
opponenet. Each program had to : 

1. Move itself
2. Search out the other code that the opponent had written
3. Once the opponent code is found, you destroy it
4. You would do a 2D visualization of code in RAM, and you would see two worms swimming around the screen


