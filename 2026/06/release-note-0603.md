
# Title: June 02, 2026 
Link: https://docs.cloud.google.com/release-notes#June_02_2026<br>
リリースノートの本文が提供されていないため、具体的な影響調査と回答ができません。

お手数ですが、Cloud SDK の `Change` カテゴリに関するリリースノートの本文（原文）をご提供いただけますでしょうか。
本文をご提供いただければ、指定のフォーマットに沿って詳細な調査と回答を行います。
# Title: June 01, 2026 
Link: https://docs.cloud.google.com/release-notes#June_01_2026<br>
# BigQuery

## Change
原文: The Facebook Ads connector for the BigQuery Data Transfer Service now supports data transfers from the following Facebook Ads reports:

- `AdInsightsMMM`
- `Ads`
- `AdCreatives`
- `AdSets`
- `Campaigns`
- `AdImages`
- `AdLabels`
- `Businesses`
- `CustomAudiences`

説明: BigQuery Data Transfer ServiceのFacebook Adsコネクタが機能強化され、新たに以下のFacebook広告レポートタイプからのデータ転送をサポートするようになりました。これにより、より多様なFacebook広告関連データをBigQueryへ自動的に取り込むことが可能になります。

追加されたレポートタイプ:
*   `AdInsightsMMM`: 広告のインサイトデータ（複数メディア間マーケティング計測用）
*   `Ads`: 広告ごとのパフォーマンスデータ
*   `AdCreatives`: 広告クリエイティブ（画像、テキストなど）に関するデータ
*   `AdSets`: 広告セットごとのパフォーマンスデータ
*   `Campaigns`: キャンペーンごとのパフォーマンスデータ
*   `AdImages`: 広告で使用されている画像に関するデータ
*   `AdLabels`: 広告に適用されたカスタムラベルに関するデータ
*   `Businesses`: Facebookビジネスマネージャーのビジネスに関するデータ
*   `CustomAudiences`: カスタムオーディエンスに関するデータ

影響有無: 影響はありません。
この変更は、既存のFacebook Adsコネクタに新しいレポートタイプからのデータ転送機能が追加されたものであり、既存の転送設定やデータ取り込みに悪影響を与えるものではありません。新しい機能が必要な場合にのみ影響します。

対処方法:
*   **BigQuery Data Transfer ServiceのFacebook Adsコネクタを現在利用していない、または今回追加されたレポートタイプを転送する必要がない場合:** 特に対応は不要です。
*   **今回追加されたレポートタイプ（例: `AdCreatives` や `CustomAudiences`）からのデータ転送をBigQueryで行いたい場合:**
    BigQuery Data Transfer Serviceの転送設定を新規作成するか、既存の設定を更新して、これらの新しいレポートタイプを選択する必要があります。詳細は[BigQuery Data Transfer ServiceのFacebook Ads転送設定ドキュメント](https://cloud.google.com/bigquery/docs/facebook-ads-transfer)を参照してください。

用語説明:
*   **BigQuery Data Transfer Service**: BigQueryにデータを自動的に取り込むためのサービスです。SaaSアプリケーション（例: Google Ads, YouTube, Salesforce）や外部ストレージ（例: Amazon S3）などから、定期的に大量のデータをBigQueryに転送する際に利用されます。
*   **Facebook Ads connector**: BigQuery Data Transfer Serviceが提供するコネクタの一つで、Facebook広告プラットフォームからBigQueryへ広告データ（パフォーマンスデータ、クリエイティブ情報など）を自動転送するために使用されます。
*   **レポートタイプ**: Facebook広告プラットフォームで提供される様々な種類のデータカテゴリを指します。広告のパフォーマンス、オーディエンス情報、キャンペーン詳細など、目的に応じて異なるレポートタイプが用意されています。