package ui; // Eğer farklı bir paket açtıysan burayı değiştir

import javax.swing.*;
import javax.swing.border.CompoundBorder;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MainFrame extends JFrame {

    // --- RENK PALETİ (MARMARA MAVİSİ TEMASI) ---
    private final Color COLOR_BG_MAIN = Color.decode("#ECF0F1");    // Çok açık gri (Arka plan)
    private final Color COLOR_HEADER = Color.decode("#2C3E50");     // Koyu Lacivert (Başlık)
    private final Color COLOR_ACCENT = Color.decode("#3498DB");     // Canlı Mavi (Butonlar)
    private final Color COLOR_ACCENT_HOVER = Color.decode("#2980B9"); // Butonun üzerine gelinceki rengi
    private final Color COLOR_TEXT_DARK = Color.decode("#2C3E50"); // Koyu etiket yazıları
    private final Color COLOR_INPUT_BG = Color.WHITE;               // Input kutusu arka planı
    private final Color COLOR_INPUT_BORDER = new Color(200, 200, 200); // İnce gri kenarlık

    // --- FONT AYARLARI ---
    // Windows'ta modern görünen 'Segoe UI' kullanıyoruz. Yoksa 'Arial' devreye girer.
    private final Font FONT_TITLE = new Font("Segoe UI", Font.BOLD, 26);
    private final Font FONT_LABEL = new Font("Segoe UI", Font.BOLD, 14);
    private final Font FONT_INPUT = new Font("Segoe UI", Font.PLAIN, 15);
    private final Font FONT_BUTTON = new Font("Segoe UI", Font.BOLD, 16);

    // --- BİLEŞENLER ---
    private JTextField txtAdSoyad, txtEmail, txtTelefon, txtBolum;
    private JTextArea txtOzet;
    private JButton btnKaydet;

    public MainFrame() {
        // 1. Pencere Temel Ayarları
        setTitle("CV Master - Profesyonel CV Oluşturucu");
        setSize(500, 750); // Pencere boyutu (Genişlik, Yükseklik)
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null); // Absolute Layout (Öğeleri elle yerleştireceğiz)
        setResizable(false); // Tasarım bozulmaması için boyutu sabitliyoruz
        getContentPane().setBackground(COLOR_BG_MAIN); // Ana arka plan rengi

        initUI(); // Arayüzü çizdiren metodu çağır
    }

    private void initUI() {
        // --- A) BAŞLIK PANELİ (HEADER) ---
        JPanel headerPanel = new JPanel();
        headerPanel.setBounds(0, 0, 500, 90); // En üste yerleşir
        headerPanel.setBackground(COLOR_HEADER);
        headerPanel.setLayout(null);
        add(headerPanel);

        JLabel lblTitle = new JLabel("Yeni CV Oluştur");
        lblTitle.setForeground(Color.WHITE);
        lblTitle.setFont(FONT_TITLE);
        lblTitle.setBounds(30, 25, 400, 40);
        headerPanel.add(lblTitle);

        // --- B) FORM ALANLARI ---
        // Koordinatları (Y eksenini) aşağı doğru artırarak yerleştiriyoruz.
        int startY = 120; // Başlangıç Y koordinatı
        int gapY = 80;    // Her alan arasındaki boşluk

        // 1. Ad Soyad
        createStyledLabel("Ad Soyad:", 30, startY);
        txtAdSoyad = createStyledTextField(30, startY + 30, 430, 40);
        add(txtAdSoyad);

        // 2. E-Posta
        createStyledLabel("E-Posta Adresi:", 30, startY + gapY);
        txtEmail = createStyledTextField(30, startY + gapY + 30, 430, 40);
        add(txtEmail);

        // 3. Telefon
        createStyledLabel("Telefon Numarası:", 30, startY + gapY * 2);
        txtTelefon = createStyledTextField(30, startY + gapY * 2 + 30, 430, 40);
        add(txtTelefon);

        // 4. Bölüm
        createStyledLabel("Bölüm / Üniversite:", 30, startY + gapY * 3);
        txtBolum = createStyledTextField(30, startY + gapY * 3 + 30, 430, 40);
        add(txtBolum);

        // 5. Özet (TextArea farklı olduğu için ayrı yapıyoruz)
        createStyledLabel("Kısa Özet / Hedefler:", 30, startY + gapY * 4);

        txtOzet = new JTextArea();
        txtOzet.setFont(FONT_INPUT);
        txtOzet.setLineWrap(true); // Satır sonuna gelince alt satıra geç
        txtOzet.setWrapStyleWord(true);
        // İç boşluk (Padding) ekleme
        txtOzet.setBorder(new EmptyBorder(10, 10, 10, 10));

        // Scroll Pane (Kaydırma çubuğu) içine alıyoruz
        JScrollPane scrollPane = new JScrollPane(txtOzet);
        scrollPane.setBounds(30, startY + gapY * 4 + 30, 430, 100);
        // Dış çerçeve rengini inputlarla aynı yapalım
        scrollPane.setBorder(new LineBorder(COLOR_INPUT_BORDER, 1));
        add(scrollPane);


        // --- C) KAYDET BUTONU ---
        btnKaydet = new JButton("KAYDET VE OLUŞTUR");
        btnKaydet.setBounds(100, 650, 300, 50); // Alt ortaya yerleştir
        setupModernButton(btnKaydet); // Butonu modernleştiren metodu çağır

        // Buton Tıklama Olayı (Şimdilik sadece mesaj gösteriyor)
        btnKaydet.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String isim = txtAdSoyad.getText();
                if(isim.isEmpty()) {
                    JOptionPane.showMessageDialog(null, "Lütfen en azından Ad Soyad giriniz!", "Uyarı", JOptionPane.WARNING_MESSAGE);
                } else {
                    // BURAYA İLERİDE VERİTABANI KODU GELECEK
                    JOptionPane.showMessageDialog(null, "Kayıt Başarılı!\nKişi: " + isim);
                }
            }
        });
        add(btnKaydet);
    }

    // --- YARDIMCI METOTLAR (Kod Tekrarını Önlemek İçin) ---

    // 1. Modern Etiket Oluşturucu
    private void createStyledLabel(String text, int x, int y) {
        JLabel label = new JLabel(text);
        label.setBounds(x, y, 250, 25);
        label.setFont(FONT_LABEL);
        label.setForeground(COLOR_TEXT_DARK);
        add(label);
    }

    // 2. Modern Text Field Oluşturucu (En önemli kısım burası)
    private JTextField createStyledTextField(int x, int y, int width, int height) {
        JTextField field = new JTextField();
        field.setBounds(x, y, width, height);
        field.setFont(FONT_INPUT);
        field.setBackground(COLOR_INPUT_BG);
        // Kenarlık ve İç Boşluk (Padding) Ayarı
        // Dışta ince gri çizgi, içte 10px boşluk
        field.setBorder(new CompoundBorder(
                new LineBorder(COLOR_INPUT_BORDER, 1),
                new EmptyBorder(5, 10, 5, 10)));
        return field;
    }

    // 3. Butonu Modernleştiren Ayarlar
    private void setupModernButton(JButton btn) {
        btn.setFont(FONT_BUTTON);
        btn.setBackground(COLOR_ACCENT); // Canlı mavi arka plan
        btn.setForeground(Color.WHITE);  // Beyaz yazı
        btn.setFocusPainted(false);      // Tıklayınca çıkan çirkin odaklanma çizgisini kaldır
        btn.setBorderPainted(false);     // Kabartmalı kenarlığı kaldır (Düz tasarım)
        btn.setCursor(new Cursor(Cursor.HAND_CURSOR)); // Üzerine gelince el işareti çıksın

        // Hover Efekti (Üzerine gelince renk değişimi)
        btn.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                btn.setBackground(COLOR_ACCENT_HOVER); // Rengi koyulaştır
            }

            @Override
            public void mouseExited(MouseEvent e) {
                btn.setBackground(COLOR_ACCENT); // Rengi normale döndür
            }
        });
    }


    // --- MAIN METODU (Çalıştırmak için) ---
    // MainFrame.java dosyasının en altı:
    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception ignored) {}

        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                // Program başladığında artık MainFrame değil, LoginFrame açılıyor.
                new LoginFrame().setVisible(true);
            }
        });
    }
}