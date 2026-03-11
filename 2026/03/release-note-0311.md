
# Title: March 10, 2026 
Link: https://docs.cloud.google.com/release-notes#March_10_2026<br>
Google Cloudのリリースノート調査結果をご報告します。

# Cloud Composer
## Announcement
**原文:**
```
Cloud Composer 2 environments can no longer be created in
Turin (europe-west12). We're switching this region to supporting only
Cloud Composer 3 environments.
```

**説明:**
Cloud Composer 2 環境について、Turin (europe-west12) リージョンでの新規作成が不可能になる旨のアナウンスです。このリージョンは今後、Cloud Composer 3 環境のみをサポートするように変更されます。既存の Cloud Composer 2 環境がこのリージョンで稼働している場合は影響を受けませんが、新規作成はできなくなります。

**影響有無:**
**限定的な影響あり**

貴社でご利用中のCloud Composer環境はComposer 2 (Compoer version 2.7.1)です。
このアナウンスは、特定のリージョン `europe-west12` におけるCloud Composer 2環境の**新規作成**にのみ影響します。

*   現在、`europe-west12` リージョンにCloud Composer 2環境をデプロイしておらず、今後もこのリージョンに新規デプロイメントの計画がない場合は、直接的な影響はありません。
*   もし、将来的に`europe-west12` リージョンでCloud Composer 2環境の新規作成を計画している場合、そのデプロイメントは不可能となります。この場合は、代替のリージョンを検討する必要があります。
*   既存のCloud Composer 2環境が`europe-west12` リージョン以外で稼働している場合は、運用に影響はありません。

**対処方法:**
*   もし将来的にTurin (`europe-west12`) リージョンでCloud Composer 2環境を新規作成する計画がある場合は、他の利用可能なリージョンでのデプロイを検討してください。
*   または、長期的な視点として、Cloud Composer 3へのアップグレードを検討することも一案です。Cloud Composer 3はパフォーマンスや費用面での改善が図られています。

**用語説明:**
*   **Cloud Composer**: Google Cloud が提供するフルマネージドな Apache Airflow サービスです。ワークフローのオーケストレーションを容易にします。
*   **Apache Airflow**: プログラムによって複雑なワークフローをオーサリング、スケジューリング、モニタリングするためのオープンソースプラットフォームです。
*   **リージョン (Region)**: Google Cloud のリソースがホストされる特定の地理的場所を指します。データの物理的な配置を決定し、レイテンシやレジリエンスに影響します。
*   **`europe-west12` (Turin)**: イタリアのトリノに位置するGoogle Cloudのリージョンコードです。