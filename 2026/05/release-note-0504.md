
# Title: April 30, 2026 
Link: https://docs.cloud.google.com/release-notes#April_30_2026<br>
はい、承知いたしました。Google Cloudのリリースノートに基づき、各製品・アナウンス単位で影響有無、対処方法を調査し、簡潔に回答いたします。

---

# BigQuery

## Breaking

原文:
Starting May 7, 2026, new transfer configurations that transfer data from Google Ads using the BigQuery Data Transfer Service will require Multi-factor authentication (MFA) for individual user authentication.
For more information, see May 7, 2026.

[Multi-factor authentication (MFA) for individual user authentication](https://ads-developers.googleblog.com/2026/04/multi-factor-authentication-requirement.html)
[May 7, 2026](https://docs.cloud.google.com/bigquery/docs/transfer-changes#May7-google-ads)

説明：
2026年5月7日以降、Google AdsからBigQuery Data Transfer Service (DTS) を利用してデータを転送する**新しい**転送設定を作成する際に、個人のユーザー認証に対して多要素認証（MFA）が必須となります。これはセキュリティ強化のための変更です。

影響有無：
**影響あり**
- **既存の転送設定への直接的な影響は限定的**: 「new transfer configurations」とあるため、既存の転送設定が2026年5月7日以降に直ちにMFAを要求されるわけではありません。しかし、将来的な変更の可能性もゼロではありません。
- **新規の転送設定への影響あり**: 2026年5月7日以降にGoogle AdsからBigQueryへの新しいDTS転送設定を作成する場合、その設定を行うユーザーアカウントにはMFAが有効になっている必要があります。
- **Google Cloud Composerとの関連**: もし、Google Cloud Composer (Airflow DAG) がBigQuery Data Transfer Serviceを呼び出してGoogle Adsのデータ転送設定を作成するようなワークフローを実装している場合、そのワークフローを実行するサービスアカウントではなく、認証に使用する個人のGoogleアカウントにMFA設定が求められます。

対処方法：
- **既存の転送設定の確認**: 現在、BigQuery DTSでGoogle Adsからのデータ転送を利用している場合は、使用しているユーザーアカウント（サービスアカウントではなく、個人のGoogleアカウントの場合）がMFAを有効にしているか確認してください。
- **新規設定の準備**: 2026年5月7日以降にGoogle Adsからの新しいデータ転送設定を作成する予定がある場合、またはGoogle Cloud Composer等からそのような設定をプログラム的に行う場合は、その設定に使用する個人のGoogleアカウントでMFAを有効にする計画を立て、期日までに準備を完了してください。
- **公式ドキュメントの確認**: 既存の転送設定への影響を含む詳細情報については、リンク先の公式ドキュメント（特に `May 7, 2026`）を定期的に確認し、今後の更新に注意してください。

用語説明：
- **BigQuery Data Transfer Service (DTS)**: BigQueryへデータを自動的にロード・転送するためのサービス。様々なデータソース（Google Ads, Google Analytics, YouTubeなど）からのデータ収集を簡素化します。
- **多要素認証 (MFA)**: パスワードに加えて、スマートフォンアプリによるコードや生体認証など、複数の異なる認証要素を組み合わせて本人確認を行うセキュリティ手法。アカウントの不正アクセス防止に非常に有効です。
- **Breaking Change**: 既存のシステムやアプリケーションの互換性を損なう可能性のある変更。通常、何らかの対応が必要となります。

---

# Cloud SQL for PostgreSQL

## Fixed

原文:
Cloud SQL has made the following enhancements to expand the list of eligible Cloud SQL Enterprise Plus edition instances that support planned operations with near-zero downtime.

[near-zero downtime](https://docs.cloud.google.com/sql/docs/postgres/availability#near-zero-downtime)
- Instances with connector enforcement enabled are eligible for planned operations with near-zero downtime.
- Instances that use private services access with a non-RFC 1918 IP address are eligible for planned operations with near-zero downtime.

[connector enforcement enabled](https://docs.cloud.com/sql/docs/postgres/connect-connectors#enforce)
[private services access](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access)

説明：
Cloud SQL for PostgreSQLのEnterprise Plusエディションにおいて、計画的なメンテナンス（例：マイナーバージョンアップグレード）におけるニアゼロダウンタイム（極めて短いダウンタイム）の対象となるインスタンスの条件が拡大されました。これにより、以下の条件を満たすインスタンスもニアゼロダウンタイムの恩恵を受けられるようになります。
1. コネクタエンフォースメントが有効なインスタンス
2. 非RFC 1918 IPアドレスを使用したプライベートサービスアクセスを利用しているインスタンス

影響有無：
**影響なし（ポジティブな改善）**
- **間接的な恩恵あり**: Cloud SQL Enterprise Plusエディションを利用しており、かつ上記の条件に該当するインスタンスを使用している場合、計画的なメンテナンス時のダウンタイムがさらに短縮される可能性があります。これは、運用の可用性向上に寄与するポジティブな変更であり、ユーザー側で特に修正や対応は不要です。
- **Google Cloud Composerとの関連**: Google Cloud Composerのメタデータストアや、ComposerからアクセスするアプリケーションのデータベースとしてCloud SQL for PostgreSQL Enterprise Plusエディションを利用している場合、メンテナンス時の影響が軽減される可能性があります。

対処方法：
- ユーザー側で直接的に必要な対処はありません。これは既存の制限が緩和され、サービス提供側が提供する機能が向上したことを意味します。
- もし、以前これらの条件のためにニアゼロダウンタイムの対象外だったインスタンスがある場合、今後はその恩恵を受けられるため、運用計画の見直しを検討しても良いでしょう。

用語説明：
- **Cloud SQL Enterprise Plus Edition**: Cloud SQLの最上位エディションで、高いパフォーマンス、可用性、セキュリティ機能を提供します。
- **ニアゼロダウンタイム**: 計画されたメンテナンス作業中に発生するサービスの停止時間を極めて短く抑えること。データベースの可用性を最大化するための重要な機能です。
- **コネクタエンフォースメント**: Cloud SQLインスタンスへの接続に、Cloud SQL Auth ProxyなどのCloud SQLコネクタの利用を強制するセキュリティ機能。これにより、安全な接続が保証されます。
- **プライベートサービスアクセス**: Google Cloudのサービス（Cloud SQLなど）とユーザーのVirtual Private Cloud (VPC) ネットワーク間で、プライベートIPアドレスのみを使用して接続を確立するVPCネットワークピアリング機能。インターネットを経由せず、よりセキュアで高速な通信を可能にします。
- **RFC 1918**: プライベートネットワーク向けに予約されたIPアドレス範囲を定義する標準規格。非RFC 1918 IPアドレスは、通常パブリックIPアドレスとして割り当てられる範囲のIPアドレスを指しますが、プライベートサービスアクセスではVPCネットワーク内でプライベートに利用されることがあります。