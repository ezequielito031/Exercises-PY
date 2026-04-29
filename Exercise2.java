import java.util.List;

interface HasStatus {
    String getStatus();
}

class Student implements HasStatus {
    protected String name;
    protected double gpa;
    protected boolean isActive;

    public Student(String name, double gpa) {
        this.name = name;
        this.gpa = gpa;
        this.isActive = true;
    }

    @Override
    public String getStatus() {
        String status = isActive ? "Active" : "Inactive";
        return name + " is currently " + status + " with a " + gpa + " GPA.";
    }
}

class GradStudent extends Student {
    private String researchLab;

    public GradStudent(String name, double gpa, String researchLab) {
        super(name, gpa);
        this.researchLab = researchLab;
    }

    @Override
    public String getStatus() {
        return super.getStatus() + " They research in the " + researchLab + " lab.";
    }
}

class Robot implements HasStatus {
    @Override
    public String getStatus() {
        return "BEEP BOOP. Robot systems nominal.";
    }
}

public class Exercises {

    public static void main(String[] args) {
        System.out.println("--- Exercise 1 & 2: Classes and Inheritance ---");

        Student student1 = new Student("John Doe", 2.8);
        GradStudent student2 = new GradStudent("Jane Smith", 4.0, "Cybersecurity");

        System.out.println(student1.getStatus());
        System.out.println(student2.getStatus());

        System.out.println("\n--- Exercise 3: Polymorphism ---");

        List<HasStatus> entities = List.of(
            new Student("Alice", 3.5),
            new GradStudent("Bob", 3.9, "AI Data"),
            new Robot()
        );

        for (HasStatus entity : entities) {
            System.out.println(entity.getStatus());
        }
    }
}
