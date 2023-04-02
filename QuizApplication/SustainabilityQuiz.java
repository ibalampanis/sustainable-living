import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.FileNotFoundException;


public class SustainabilityQuiz {
    // define enum class Answer & hold unchangeable answers and their properties
    public enum Answer {
        Never("a", 0),
        Sometimes("b", 1),
        Always("c", 2);

        private final String reply;
        private final int points;

        Answer(String reply, int points) {
            this.reply = reply;
            this.points = points;
        }

        public String getReply() {
            return reply;
        }

        public int getPoints() {
            return points;
        }
    }

    public static void main(String[] args) throws IOException {
        // read and fetch the questions from the txt file and use a delimiter to hold them in questions array
        try {
            List<String> data = new ArrayList<String>();
            Scanner sc = new Scanner(new FileReader("Questions.txt"))
                    .useDelimiter("!\\s*");
            String str;
            while (sc.hasNext()) {
                str = sc.next();
                data.add(str);
            }
            String[] questions = data.toArray(new String[0]);
            sc.close();
            startQuiz(questions);
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }
    }

    public static void startQuiz(String[] questions) {
        int result = 0;
        Scanner keyboard = new Scanner(System.in);
        System.out.println("************** Answer 20 questions and find out if " +
                "your lifestyle is sustainable. **************");
        System.out.println();
        System.out.println("Do you...");
        System.out.println();
        for (int i = 0; i < questions.length; i++) {
            System.out.println(i + 1 + "." + questions[i] + "?");
            Answer[] answers = Answer.values();
            for (Answer a : answers) {
                System.out.println(a.getReply() + ". " + a);
            }
            System.out.println();
            System.out.println("Enter your answer");
            String answer = keyboard.nextLine().toLowerCase();
            while (!((answer.equals("a")) || answer.equals("b") || answer.equals("c"))) {
                System.out.println();
                System.out.println("Error while entering your answer.");
                System.out.println("Please try again!");
                System.out.println();
                System.out.println("Provide 'a' for Never.");
                System.out.println("Provide 'b' for Sometimes.");
                System.out.println("Provide 'c' for Always.");
                System.out.println();
                System.out.println(i + 1 + "." + questions[i] + "?");
                for (Answer a : answers) {
                    System.out.println(a.getReply() + ". " + a);
                }
                System.out.println();
                System.out.println("Enter your answer");
                answer = keyboard.nextLine().toLowerCase();
            }
            if (answer.equals(Answer.Sometimes.getReply())) {
                result += Answer.Sometimes.getPoints();
            } else if (answer.equals(Answer.Always.getReply())) {
                result += Answer.Always.getPoints();
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("************** You gathered " + result + " points **************");
        System.out.println();
        if (result < 12) {
            System.out.println("Have you even heard about climate change and" +
                    " the planetary threat? If so, you are not giving it the " +
                    "priority it deserves.As the class teacher would say – Must Do Better!");
        } else if (result < 20) {
            System.out.println("You are already doing a few basic things – but " +
                    "there is so much more that you could be doing to show your" +
                    " concern for the environment. Note some of the tips in our" +
                    " quiz – and start to implement them");
        } else if (result <= 34) {
            System.out.println("You demonstrate a good environmental conscience" +
                    " – but there’s still room for improvement, so look at the " +
                    "questions where you scored badly and make some changes");

        } else {
            System.out.println("Wow, you certainly know your Greens. If you " +
                    "scored this highly, you can rightly call yourself a Green " +
                    "Champion – well done and keep up the good work!");
        }
    }
}
