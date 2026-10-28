import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Label oluşturduk
        Label label = new Label("Selam kral, JavaFX çalışıyor!");

        // Label'ı ekranda göstermek için layout
        StackPane root = new StackPane();
        root.getChildren().add(label);

        // Scene oluşturuyoruz: root ve boyut
        Scene scene = new Scene(root, 400, 200);

        // Stage (pencere) ayarları
        primaryStage.setTitle("JavaFX Deneme");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
