
# Title: February 24, 2026 
Link: https://docs.cloud.google.com/release-notes#February_24_2026<br>
Google Cloud インフラエンジニアとして、リリースノートの変更点について、構築済みのサービスへの影響有無を調査し、以下の通りご報告いたします。

---

# Apigee X
Apigee Xについては、お客様環境に自動的に適用される変更が主であり、特段の対応は不要です。しかし、セキュリティ修正やバグ修正が含まれておりますので、プラットフォームの安定性向上に寄与します。

## Announcement
原文: On February 24th, 2026, we released an updated version of Apigee (1-17-0-apigee-3).
> Note: Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：Apigee の新しいバージョン `1-17-0-apigee-3` がリリースされました。このリリースは、本日より Google Cloud の全てのゾーンへ順次展開されており、完了までには4営業日以上かかる場合があります。リリースが完了するまでは、お客様のインスタンスで新機能や修正が利用できない可能性があります。

影響有無：**軽微な影響あり（ポジティブ）**
Apigee X は Google Cloud が管理するマネージドサービスであるため、バージョンアップは自動的に実施されます。お客様側での手動によるバージョンアップ作業は不要です。ロールアウト期間中は、新機能や修正がすぐに利用できない可能性があるという一時的な制約があるものの、サービスの継続性には影響しません。

対処方法：**不要**
サービス側で自動的に適用されるため、お客様側での対処は不要です。ロールアウトが完了するまでお待ちください。

## Security
原文: Security fix for Apigee infrastructure. This addresses the following vulnerabilities:
- CVE-2025-61730
- CVE-2025-68156
- CVE-2025-54388
- CVE-2025-61727
- CVE-2025-61729
(各CVEへのリンクは省略)

説明：Apigee インフラストラクチャに対する複数のセキュリティ脆弱性（CVE-2025-61730、CVE-2025-68156、CVE-2025-54388、CVE-2025-61727、CVE-2025-61729）が修正されました。

影響有無：**影響なし（ポジティブ）**
プラットフォームレベルでのセキュリティ脆弱性修正であり、お客様のApigee環境のセキュリティ体制が自動的に強化されます。既存のワークロードにマイナスの影響を与えることはなく、むしろ安全性が向上します。

対処方法：**不要**
Google Cloud によって自動的に適用されるため、お客様側での対処は不要です。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: サイバーセキュリティの脆弱性に関する公開された情報に一意の識別子を付与し、共通の形式で情報を提供する国際的な標準です。これにより、脆弱性情報の共有と理解が容易になります。

## Fixed
原文:
*   Fixed a memory leak which could result in a spike in 503 responses with `no_healthy_upstream` messages.
*   Applied a fix for proxy calls failing with `The URI contains illegal characters` error after Netty upgrade.
*   Fixed an issue resulting in TLS handshake errors.

説明：以下のバグが修正されました。
*   メモリリークが原因で `no_healthy_upstream` メッセージを伴う503エラー（Service Unavailable）が急増する可能性があった問題。
*   Netty アップグレード後に `The URI contains illegal characters` エラーによりプロキシ呼び出しが失敗する問題。
*   TLS ハンドシェイクエラーが発生する問題。

影響有無：**影響なし（ポジティブ）**
これらの修正は、Apigee X の安定性と信頼性を向上させます。お客様の既存のワークロードにマイナスの影響はありません。もし、これらの問題に過去に遭遇していた場合は、本修正によりサービス可用性が改善されることが期待されます。

対処方法：**不要**
サービス側で自動的に適用されるため、お客様側での対処は不要です。

用語説明：
*   **503 Service Unavailable**: HTTPステータスコードの一つで、サーバーが一時的に過負荷またはメンテナンス中のため、リクエストを処理できないことを示します。
*   **`no_healthy_upstream`**: API Gatewayやロードバランサーがバックエンドサービス（upstream）に対して健全な接続を見つけられない場合に発生するエラーメッセージ。通常、バックエンドサービスの障害や過負荷を示唆します。
*   **Netty**: 高性能なネットワークアプリケーション開発のための非同期イベント駆動型ネットワークアプリケーションフレームワークです。
*   **TLS ハンドシェイク**: Transport Layer Security (TLS) プロトコルにおいて、クライアントとサーバーが暗号化された通信を開始する前に、お互いを認証し、暗号化キーを交換するプロセスです。このプロセスに失敗すると、セキュアな通信が確立できません。

---

# Google Kubernetes Engine (GKE)
GKEに関する変更は、料金体系に関するものであり、お客様のコスト最適化に貢献する可能性があります。

## Change
原文: Expanded coverage for compute flexible committed use discounts (CUDs) is available to all Cloud Billing accounts. All Cloud Billing accounts have been automatically migrated to the new spend-based CUD model and you no longer need to opt in to benefit from the expanded coverage. For the full list of eligible SKUs across Compute Engine, GKE, and Cloud Run, see SKU Groups - Compute Flexible CUD Eligible SKUs. To learn more about compute flexible CUDs and how they apply to your GKE usage, see the GKE CUDs documentation.
(各ドキュメントへのリンクは省略)

説明：コンピュートサービス（Compute Engine、GKE、Cloud Run）向けの柔軟なコミットメント利用割引（CUDs）の適用範囲が、全ての Cloud Billing アカウントに拡大されました。既存のCloud Billingアカウントは、新しい消費ベースのCUDモデルへ自動的に移行され、特別なオプトイン作業なしで拡大された割引対象の恩恵を受けられるようになります。割引が適用されるSKUの完全なリストは、SKU Groups - Compute Flexible CUD Eligible SKUs ドキュメントで確認できます。GKE利用におけるCUDsの適用方法については、GKE CUDs ドキュメントを参照してください。

影響有無：**影響あり（ポジティブ、料金体系の変更）**
これは料金体系に関する重要な変更です。お客様がGKE、Compute Engine、Cloud Runを利用している場合、既存の利用料金に対して自動的に割引が適用される可能性が高まります。特に、既にCUDを利用している場合や、コミットメントを検討している場合には、より柔軟な形で割引の恩恵を受けられるようになります。手動での操作は不要ですが、コスト最適化の機会となります。

対処方法：**推奨あり**
自動的に適用されるため、緊急の対処は不要です。しかし、この変更がお客様のGKEおよび関連するコンピュートサービスの利用料金にどのように影響するかを理解するため、以下のドキュメントを確認し、請求状況を監視することをお勧めします。
*   [新消費ベースCUDモデルに関するドキュメント](https://cloud.google.com/docs/cuds-multiprice)
*   [Compute Flexible CUD 対象SKUグループリスト](https://cloud.google.com/skus/sku-groups/compute-flexible-cud-eligible-skus)
*   [GKE CUDs ドキュメント](https://cloud.google.com/kubernetes-engine/cud)
これにより、将来的な費用計画やコスト最適化戦略を検討する上で役立ちます。

用語説明：
*   **Committed Use Discounts (CUDs)**: Google Cloud におけるコミットメント利用割引のことです。特定の Google Cloud サービスのリソース使用量を一定期間（通常1年または3年）コミットすることで、オンデマンド料金よりも大幅な割引を受けられる料金モデルです。
*   **Compute Flexible CUDs**: Compute Engine、Google Kubernetes Engine (GKE)、Cloud Run といったコンピュートサービス全体で適用される柔軟なCUDモデルです。特定のVMタイプやリージョンに縛られず、対象となるコンピュートリソースの利用合計量に対して割引が適用されます。
*   **Spend-based CUD model**: 消費ベースのCUDモデルです。従来のリソースベースのCUDが特定のCPUコア数やメモリ量などのリソースにコミットするのに対し、消費ベースでは特定のサービスグループにおける費用の総額をコミットすることで割引が適用されます。これにより、利用するリソースの種類が変化しても割引が適用されやすくなります。
*   **SKU (Stock Keeping Unit)**: クラウドサービスにおける個々のサービスやリソース（例：特定のVMインスタンスタイプ、ストレージ量、ネットワーク転送量など）を識別するための単位です。料金設定の最小単位となります。