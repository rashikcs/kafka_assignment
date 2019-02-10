#Simple Kafka Assignment

Program (!) Two Kafka Producers writing to the same topic (Python)

Producer A writes even numbers every second, the other producer B writes off numbers every two seconds to the topic.

Your consumer C reads the numbers and prints them with the origin A or B.

In practice: You start the eg three Python scripts independently by running start.bat file which will run the 
consumer C background and Producer A and B separately on a new window. (First you stront the zookeper and the Kafka server