
class CMyString
{
  public:
    CMyString(char *pData = nullptr);
    CMyString(const CMyString &str);
    ~CMyString(void);

  private:
    char *m_pData;
}
