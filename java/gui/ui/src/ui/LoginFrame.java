package ui;

import javax.swing.*;
import javax.swing.border.CompoundBorder;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class LoginFrame extends JFrame {

    // --- RENK PALETİ ---
    // ARKA PLAN GRADYAN RENKLERİ (Soldan Sağa)
    private final Color COLOR_GRADIENT_START = Color.decode("#D7DDE8"); // Sol taraf (Hafif koyu gri-mavi)
    private final Color COLOR_GRADIENT_END = Color.decode("#ECF0F1");   // Sağ taraf (Daha açık)

    private final Color COLOR_HEADER = Color.decode("#2C3E50");     // Koyu Lacivert Başlık
    private final Color COLOR_ACCENT = Color.decode("#3498DB");     // Mavi Buton
    private final Color COLOR_ACCENT_HOVER = Color.decode("#2980B9"); // Buton Hover
    private final Color COLOR_TEXT_DARK = Color.decode("#2C3E50"); // Koyu yazılar
    private final Color COLOR_INPUT_BG = Color.WHITE;               // Input arka planı
    private final Color COLOR_INPUT_BORDER = new Color(200, 200, 200); // Input kenarlık

    // Fontlar
    private final Font FONT_TITLE = new Font("Segoe UI", Font.BOLD, 24);
    private final Font FONT_LABEL = new Font("Segoe UI", Font.BOLD, 14);
    private final Font FONT_INPUT = new Font("Segoe UI", Font.PLAIN, 15);
    private final Font FONT_BUTTON = new Font("Segoe UI", Font.BOLD, 16);

    // Bileşenler
    private JTextField txtUsername;
    private JPasswordField txtPassword;

    public LoginFrame() {
        setTitle("Giriş Yap - CV Master");
        setSize(400, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        setLocationRelativeTo(null);

        // --- ÖZEL ARKA PLAN (GRADYAN) AYARI ---
        JPanel gradientContentPane = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Graphics2D g2d = (Graphics2D) g;
                g2d.setRenderingHint(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);

                int w = getWidth();
                int h = getHeight();

                // YATAY GRADYAN FIRÇASI (Soldan Sağa)
                GradientPaint gp = new GradientPaint(0, 0, COLOR_GRADIENT_START, w, 0, COLOR_GRADIENT_END);

                g2d.setPaint(gp);
                g2d.fillRect(0, 0, w, h);
            }
        };

        gradientContentPane.setLayout(null);
        setContentPane(gradientContentPane);

        initUI();
    }

    private void initUI() {
        // --- A) BAŞLIK PANELİ (HEADER) ---
        JPanel headerPanel = new JPanel();
        headerPanel.setBounds(0, 0, 400, 80);
        headerPanel.setBackground(COLOR_HEADER);
        headerPanel.setLayout(null);

        JLabel lblTitle = new JLabel("Kullanıcı Girişi");
        lblTitle.setForeground(Color.WHITE);
        lblTitle.setFont(FONT_TITLE);
        lblTitle.setHorizontalAlignment(SwingConstants.CENTER);
        lblTitle.setBounds(0, 20, 400, 40);
        headerPanel.add(lblTitle);
        add(headerPanel);


        // --- B) GİRİŞ FORMU ---
        int startY = 140;
        int centerX = 50;

        // 1. Kullanıcı Adı
        JLabel lblUser = createStyledLabel("Kullanıcı Adı:", centerX, startY);
        add(lblUser);

        txtUsername = createStyledTextField(centerX, startY + 30, 300, 40);
        add(txtUsername);

        // 2. Şifre
        JLabel lblPass = createStyledLabel("Şifre:", centerX, startY + 100);
        add(lblPass);

        txtPassword = new JPasswordField();
        setupModernInputField(txtPassword, centerX, startY + 130, 300, 40);
        add(txtPassword);


        // --- C) GİRİŞ BUTONU ---
        JButton btnLogin = new JButton("GİRİŞ YAP");
        btnLogin.setBounds(centerX, 350, 300, 50);
        setupModernButton(btnLogin);

        btnLogin.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String username = txtUsername.getText();
                String password = new String(txtPassword.getPassword());

                // NOT: MainFrame sınıfının projenizde var olduğundan emin olun.
                // Yoksa burası hata verir. Test için geçici olarak kapatabilirsiniz.
                if (username.equals("admin") && password.equals("1234")) {
                    try {
                        dispose(); // Login ekranını kapat
                        new MainFrame().setVisible(true); // Ana ekranı aç
                    } catch (Exception ex) {
                        JOptionPane.showMessageDialog(null, "MainFrame bulunamadı! Sadece giriş başarılı.", "Test Bilgisi", JOptionPane.INFORMATION_MESSAGE);
                    }
                } else {
                    JOptionPane.showMessageDialog(null, "Hatalı giriş!", "Hata", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
        add(btnLogin);
    }

    // --- YARDIMCI METOTLAR ---
    private JLabel createStyledLabel(String text, int x, int y) {
        JLabel label = new JLabel(text);
        label.setBounds(x, y, 250, 25);
        label.setFont(FONT_LABEL);
        label.setForeground(COLOR_TEXT_DARK);
        return label;
    }

    private JTextField createStyledTextField(int x, int y, int width, int height) {
        JTextField field = new JTextField();
        setupModernInputField(field, x, y, width, height);
        return field;
    }

    private void setupModernInputField(JTextField field, int x, int y, int width, int height) {
        field.setBounds(x, y, width, height);
        field.setFont(FONT_INPUT);
        field.setBackground(COLOR_INPUT_BG);
        field.setBorder(new CompoundBorder(
                new LineBorder(new Color(180, 180, 180), 1),
                new EmptyBorder(5, 10, 5, 10)));
    }

    private void setupModernButton(JButton btn) {
        btn.setFont(FONT_BUTTON);
        btn.setBackground(COLOR_ACCENT);
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        btn.setBorderPainted(false);
        btn.setCursor(new Cursor(Cursor.HAND_CURSOR));
        btn.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) { btn.setBackground(COLOR_ACCENT_HOVER); }
            @Override
            public void mouseExited(MouseEvent e) { btn.setBackground(COLOR_ACCENT); }
        });
    }

    // ===========================================================================
    // TEST İÇİN MAIN METODU
    // ===========================================================================
    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception ignored) {}

        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new LoginFrame().setVisible(true);
            }
        });
    }
    // Sınıf burada bitiyor. Tek bir süslü parantez olmalı.
}