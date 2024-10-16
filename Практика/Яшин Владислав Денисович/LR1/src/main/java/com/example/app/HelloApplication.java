package com.example.app;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.stage.Stage;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class HelloApplication extends Application {
    @Override public void start(Stage stage) {
        stage.setTitle("LR1");

        final NumberAxis xAxis = new NumberAxis();
        final NumberAxis yAxis = new NumberAxis();
        final LineChart<Number,Number> lineChart = new LineChart<Number,Number>(xAxis,yAxis);
        lineChart.setTitle("График функции");

        XYChart.Series series = new XYChart.Series();
        series.setName("y(x) = a1 * sin(b1 * x) + a2 * sin(b2 * x) + a3 * sin(b3 * x)");

        //Спрашиваем у пользователя данные
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введитее a1 - ");
        double a1 = scanner.nextDouble();
        System.out.println("Введитее b1 - ");
        double b1 = scanner.nextDouble();
        System.out.println("Введитее a2 - ");
        double a2 = scanner.nextDouble();
        System.out.println("Введитее b2 - ");
        double b2 = scanner.nextDouble();
        System.out.println("Введитее a3 - ");
        double a3 = scanner.nextDouble();
        System.out.println("Введитее b3 - ");
        double b3 = scanner.nextDouble();
        System.out.println("Введитее начально зачение xn - ");
        double xn = scanner.nextDouble();
        System.out.println("Введитее конечное значение xk - ");
        double xk = scanner.nextDouble();
        System.out.println("Введитее шаг dk - ");
        double dk = scanner.nextDouble();
        scanner.close();

        HelloController controller = new HelloController();
        Map<Double, Double> map = new HashMap<>(controller.func(a1,b1,a2,b2,a3,b3,xn,xk,dk));

        //Добавленние точек на график
        for(Map.Entry<Double, Double> entry : map.entrySet()) {
            series.getData().add(new XYChart.Data(entry.getKey(),entry.getValue()));
        }

        Scene scene  = new Scene(lineChart,800,600); //Размер сцены
        lineChart.getData().add(series);

        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {launch(args);}
}