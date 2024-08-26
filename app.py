from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = [{"ad": "CEO","ataid": null,"hiyerAd": "CEO","hiyerId": "1","id": 1},{"ad": "CFO","ataid": 1,"hiyerAd": "CEO/CFO","hiyerId": "1.1","id": 2},{"ad": "CTO","ataid": 1,"hiyerAd": "CEO/CTO","hiyerId": "1.2","id": 3},{"ad": "COO","ataid": 1,"hiyerAd": "CEO/COO","hiyerId": "1.3","id": 4},{"ad": "CHRO","ataid": 1,"hiyerAd": "CEO/CHRO","hiyerId": "1.4","id": 5},{"ad": "CMO","ataid": 1,"hiyerAd": "CEO/CMO","hiyerId": "1.5","id": 6},{"ad": "Finans Müdürü","ataid": 2,"hiyerAd": "CEO/CFO/Finans Müdürü","hiyerId": "1.1.1","id": 7},{"ad": "Muhasebe Müdürü","ataid": 2,"hiyerAd": "CEO/CFO/Muhasebe Müdürü","hiyerId": "1.1.2","id": 8},{"ad": "Yazılım Geliştirme Müdürü","ataid": 3,"hiyerAd": "CEO/CTO/Yazılım Geliştirme Müdürü","hiyerId": "1.2.1","id": 9},{"ad": "IT Destek Müdürü","ataid": 3,"hiyerAd": "CEO/CTO/IT Destek Müdürü","hiyerId": "1.2.2","id": 10},{"ad": "Siber Güvenlik Müdürü","ataid": 3,"hiyerAd": "CEO/CTO/Siber Güvenlik Müdürü","hiyerId": "1.2.3","id": 11},{"ad": "Operasyon Müdürü","ataid": 4,"hiyerAd": "CEO/COO/Operasyon Müdürü","hiyerId": "1.3.1","id": 12},{"ad": "Üretim Müdürü","ataid": 4,"hiyerAd": "CEO/COO/Üretim Müdürü","hiyerId": "1.3.2","id": 13},{"ad": "Tedarik Zinciri Müdürü","ataid": 4,"hiyerAd": "CEO/COO/Tedarik Zinciri Müdürü","hiyerId": "1.3.3","id": 14},{"ad": "İnsan Kaynakları Müdürü","ataid": 5,"hiyerAd": "CEO/CHRO/İnsan Kaynakları Müdürü","hiyerId": "1.4.1","id": 15},{"ad": "Eğitim ve Gelişim Müdürü","ataid": 5,"hiyerAd": "CEO/CHRO/Eğitim ve Gelişim Müdürü","hiyerId": "1.4.2","id": 16},{"ad": "İşe Alım Müdürü","ataid": 5,"hiyerAd": "CEO/CHRO/İşe Alım Müdürü","hiyerId": "1.4.3","id": 17},{"ad": "Pazarlama Müdürü","ataid": 6,"hiyerAd": "CEO/CMO/Pazarlama Müdürü","hiyerId": "1.5.1","id": 18},{"ad": "Dijital Pazarlama Müdürü","ataid": 6,"hiyerAd": "CEO/CMO/Dijital Pazarlama Müdürü","hiyerId": "1.5.2","id": 19},{"ad": "Ürün Müdürü","ataid": 6,"hiyerAd": "CEO/CMO/Ürün Müdürü","hiyerId": "1.5.3","id": 20},{"ad": "Pazarlama Uzmanı","ataid": 18,"hiyerAd": "CEO/CMO/Pazarlama Müdürü/Pazarlama Uzmanı","hiyerId": "1.5.1.1","id": 21},{"ad": "Grafik Tasarımcı","ataid": 19,"hiyerAd": "CEO/CMO/Dijital Pazarlama Müdürü/Grafik Tasarımcı","hiyerId": "1.5.2.1","id": 22},{"ad": "Yazılım Geliştirme Uzmanı","ataid": 9,"hiyerAd": "CEO/CTO/Yazılım Geliştirme Müdürü/Yazılım Geliştirme Uzmanı","hiyerId": "1.2.1.1","id": 23},{"ad": "Network Uzmanı","ataid": 10,"hiyerAd": "CEO/CTO/IT Destek Müdürü/Network Uzmanı","hiyerId": "1.2.2.1","id": 24},{"ad": "Siber Güvenlik Uzmanı","ataid": 11,"hiyerAd": "CEO/CTO/Siber Güvenlik Müdürü/Siber Güvenlik Uzmanı","hiyerId": "1.2.3.1","id": 25},{"ad": "Muhasebe Uzmanı","ataid": 8,"hiyerAd": "CEO/CFO/Muhasebe Müdürü/Muhasebe Uzmanı","hiyerId": "1.1.2.1","id": 26},{"ad": "Tedarik Uzmanı","ataid": 14,"hiyerAd": "CEO/COO/Tedarik Zinciri Müdürü/Tedarik Uzmanı","hiyerId": "1.3.3.1","id": 27}]
    
    # id=1 olan kaydın ataid değerini None olarak güncelle
    for item in data:
        if item['id'] == 1:
            item['ataid'] = None

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
