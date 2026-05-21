
# Title: May 20, 2026 
Link: https://docs.cloud.google.com/release-notes#May_20_2026<br>
以下にリリースノートの内容について、影響調査の結果をまとめます。

---

# Apigee X
## Security
原文: On May 20, 2026, we published a security bulletin for Apigee (CVE-2026-2264) where the `IntegrationRegion` parameter in the `SetIntegrationRequest` policy lacks validation, allowing for Server-Side Request Forgery (SSRF) and service account token exfiltration. The issue arises when an attacker can control a flow variable used for `IntegrationRegion`, leading to requests being sent to an attacker-controlled host with the service account token.
[CVE-2026-2264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-2264)
Security bulletin published: GCP-2026-034
[GCP-2026-034](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2026-034)

説明：Apigeeにおいて、`SetIntegrationRequest`ポリシーの`IntegrationRegion`パラメータに検証不備がある脆弱性（CVE-2026-2264）が発見されました。これにより、Server-Side Request Forgery (SSRF) やサービスアカウントトークンの外部漏洩が発生する可能性があります。攻撃者が`IntegrationRegion`に使用されるフロー変数を制御できる場合、サービスアカウントトークンを含むリクエストを攻撃者が制御するホストに送信させることが可能になります。このセキュリティ速報は2026年5月20日に公開されたと記載されていますが、これは将来の日付であり、先行アナウンスまたは誤記である可能性があります。

影響有無：Apigee Xを利用しており、`SetIntegrationRequest`ポリシーで`IntegrationRegion`パラメータにユーザー入力や動的なフロー変数を活用している場合、本脆弱性の影響を受ける可能性があります。特に、攻撃者がフロー変数を制御できるような設計になっている場合は、セキュリティリスクが高まります。

対処方法：
1.  公開されたセキュリティ速報 `GCP-2026-034` を確認し、詳細な影響範囲と推奨される対策（パッチの適用、設定変更、利用方法の見直しなど）を把握してください。
2.  Apigee環境で`SetIntegrationRequest`ポリシーの使用状況をレビューし、`IntegrationRegion`パラメータへの入力が安全に処理されているかを確認してください。可能であれば、外部からの入力や動的なフロー変数に依存しない設計に変更することを検討してください。
3.  Google Cloudからの追加のアナウンスや自動修正に関する情報がないか、公式ドキュメントやセキュリティアラートを継続的に監視してください。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアの脆弱性を一意に識別するための国際的な命名規則です。
*   **Server-Side Request Forgery (SSRF)**: 攻撃者がサーバー側で意図しないリクエストを生成させ、内部ネットワークへのアクセスや機密情報の取得などを試みる攻撃手法です。
*   **サービスアカウントトークン (Service Account Token)**: Google Cloudのサービスアカウントが、他のGoogle Cloudサービスに対して認証を行う際に使用する認証情報です。このトークンが漏洩すると、攻撃者がサービスアカウントの権限を悪用する可能性があります。
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームで、APIの設計、セキュリティ、デプロイ、監視、分析を一元的に行えます。

---

# BigQuery
## Announcement
原文: BigQuery can re-execute instructions (queries) to try to proactively detect performance, correctness, or functional regressions. These re-executions will have no side effects and will happen with no additional cost or resource consumption. Data access logs may show 'bigquery-adminbot@system.gserviceaccount.com' when BigQuery re-executes an instruction.

説明：BigQueryが、パフォーマンス、正確性、または機能の回帰をプロアクティブに検出するために、クエリなどの命令を内部的に再実行する機能を追加しました。この再実行はユーザー側への副作用がなく、追加のコストやリソース消費も発生しません。再実行時にデータアクセスログに`bigquery-adminbot@system.gserviceaccount.com`というシステムサービスアカウントが表示される場合があります。

影響有無：影響なし。
これはBigQueryの内部的な改善であり、ユーザーが実行するクエリの動作や課金には影響を与えません。追加のコストやリソース消費もないため、費用面での変更もありません。データアクセスログにシステムアカウントからのエントリが表示される可能性がある点のみ、監査ログを厳密に監視している場合に認識しておく必要があります。

対処方法：不要。
ただし、データアクセスログを監視している場合は、`bigquery-adminbot@system.gserviceaccount.com`からのログエントリがBigQueryのシステムによる正常な動作であることを認識しておくことが推奨されます。

用語説明：
*   **BigQuery**: Google Cloudが提供する、完全マネージドのエンタープライズデータウェアハウスで、ペタバイト規模のデータを分析できます。
*   **回帰 (Regression)**: ソフトウェア開発において、新しい変更が導入された結果、以前は正しく動作していた機能が誤動作したり、パフォーマンスが低下したりすることです。
*   **データアクセスログ (Data Access Logs)**: Google Cloudの監査ログの一種で、ユーザーがGoogle Cloudリソースに対してデータを作成、変更、読み取りを行った際のアクセスを記録するログです。

---

# Cloud Service Mesh
## Announcement
原文: Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the stable channel now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see Data plane extensibility with `EnvoyFilter`.
[Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility)
To troubleshoot any issue while configuring, see Resolving data plane extensibility issues.
[Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility)

説明：マネージドCloud Service Meshの安定版チャネルにおいて、`TRAFFIC_DIRECTOR`実装が`EnvoyFilter` APIの限定的なサポートを開始しました。これにより、ローカルレートリミットなどの機能で`EnvoyFilter`を利用できるようになりました。

影響有無：影響なし。
これはCloud Service Meshの新しい機能追加であり、既存のサービスメッシュの動作に自動的に影響を与えるものではありません。ユーザーが明示的に`EnvoyFilter`を設定しない限り、既存の構成やトラフィック管理に変化はありません。この機能は、データプレーンのより高度なカスタマイズを必要とする場合に、新たな選択肢を提供します。

対処方法：不要。
ただし、`EnvoyFilter`によるカスタムなトラフィック管理やポリシー適用を検討している場合は、この機能を利用してサービスメッシュの柔軟性を高めることが可能です。詳細については、提供されているドキュメントリンクを参照してください。

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供するフルマネージドなサービスメッシュで、Istioベースです。マイクロサービス間のトラフィック管理、セキュリティ、可観測性を提供します。
*   **TRAFFIC_DIRECTOR**: Google Cloudのフルマネージドなアプリケーションネットワーキングサービスで、グローバルなトラフィック管理、ロードバランシング、サービスメッシュのデータプレーン制御を統合します。
*   **EnvoyFilter API**: Istioのカスタムリソースの一つで、Envoyプロキシの構成を直接カスタマイズするためのAPIです。これにより、Envoyの低レベルな機能にアクセスし、特定の高度なトラフィック管理や可観測性のユースケースを実現できます。
*   **ローカルレートリミット (Local Rate Limiting)**: サービスメッシュ内の各Envoyプロキシ（サイドカー）が、自身を通過するリクエストのレートを個別に制限する機能です。

---

## Announcement
原文: Cloud Service Mesh can now report a status code to indicate whether an Istio API is accepted or rejected. You can view the status code on the resource and mesh state. For more information see MembershipState Error Codes.
[MembershipState Error Codes](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-configuration#membershipstate_error_codes)

説明：Cloud Service Meshが、Istio APIの設定が正常に受け入れられたか、または拒否されたかを示すステータスコードを報告するようになりました。このステータスコードは、リソースとメッシュの状態から確認できます。

影響有無：影響なし。
これは主に運用とトラブルシューティングの利便性を向上させるための機能追加です。既存のサービスメッシュの動作や設定に直接的な影響はありません。Istio APIの適用状況の可視性が向上するため、設定ミスやエラーの原因特定が容易になります。

対処方法：不要。
Istio APIの設定適用時に問題が発生した場合や、現在のメッシュの状態を把握する際に、この新しいステータスコードを利用して状況を迅速に把握できることを覚えておくと良いでしょう。

用語説明：
*   **Istio API**: Istioが提供するカスタムリソース定義（CRD）を通じて、トラフィックルーティング、セキュリティポリシー、テレメトリ設定など、サービスメッシュの動作を定義するためのAPI群です。
*   **MembershipState**: Google Cloud Service Meshにおいて、クラスタやサービスがサービスメッシュに正常に参加し、設定が適用されているかどうかの状態を示す内部的な指標です。
*   **ステータスコード (Status Code)**: APIリクエストの結果を示す数値コードで、操作の成否やその理由を簡潔に表現します。