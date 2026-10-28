public class Sarki {
    private String sarkiAdi;
    private String sarkiSanatci;
    private String album;
    private int sure;

    public Sarki(String sarkiAdi, String sarkiSanatci, String album, int sure) {
        this.sarkiAdi = sarkiAdi;
        this.sarkiSanatci = sarkiSanatci;
        this.album = album;
        this.sure = sure;
    }
    public String getSarkiAdi() {
        return sarkiAdi;
    }
    public int getSure() {
        return sure;
    }
    @Override
    public String toString() {
        return sarkiAdi+" - "+sarkiSanatci+" ( "+album+" ) | "+sure+" dk";
    }
}
