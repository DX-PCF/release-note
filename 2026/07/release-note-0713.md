
# Title: July 10, 2026 
Link: https://docs.cloud.google.com/release-notes#July_10_2026<br>
以下に、Google Kubernetes Engine (GKE) のリリースノートに対する調査結果をまとめます。お客様のGoogle Cloud Composer (Composer version 2.7.1、Airflow version 2.7.3) 環境への影響を中心に評価しました。

---

# Google Kubernetes Engine

## Change

原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)
## No channel (deprecated)

**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- The following versions are now available:

- 1.33.13-gke.1101000
- 1.34.9-gke.1287000
- 1.35.6-gke.1250000
- 1.36.0-gke.4681000
- 1.36.2-gke.1346000

- The following node versions are now available:

- 1.30.14-gke.2816000
- 1.31.14-gke.2233000
- 1.32.13-g
# Title: July 09, 2026 
Link: https://docs.cloud.google.com/release-notes#July_09_2026<br>
# Google Kubernetes Engine

## Change (GKE バージョン更新全般)
原文:
GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
... (以下、No channel (deprecated), Stable, Regular, Rapid, Extended 各チャネルの具体的なバージョン情報、非推奨バージョン、自動アップグレードターゲットが続く)

説明：
Google Kubernetes Engine (GKE) の複数のリリースチャネルにおいて、利用可能なGKEバージョンが更新されました。
具体的には以下の変更が含まれます:
*   **新しいデフォルトバージョン:** 各チャネルで新しいGKEバージョンがクラスタ作成時のデフォルトとして設定されました。
*   **新しい利用可能バージョン:** コントロールプレーンとノードプールのアップグレード、および新規クラスタ作成用に、複数の新しいGKEバージョン（例: 1.30.x, 1.31.x, 1.32.x, 1.33.x, 1.34.x, 1.35.x, 1.36.xの各パッチバージョン）が利用可能になりました。
*   **非推奨バージョン:** 複数の古いGKEバージョンが非推奨（deprecated）となり、90日以内、またはサポート終了時に削除される予定です。
*   **自動アップグレードターゲットの更新:** 各チャネルの自動アップグレードターゲットが更新され、GKEは設定に基づきクラスタを新しいマイナーバージョンまたはパッチバージョンに自動的にアップグレードする可能性があります。

影響有無：
**直接的な影響は限定的ですが、潜在的な影響と対処の必要性があります。**

*   **非推奨バージョンを使用している場合:** 現在稼働中のGKEクラスタが非推奨リストに含まれるバージョンを使用している場合、90日以内にそのバージョンが削除されるため、**強制的にアップグレードが必要になります。** これはアプリケーションの互換性問題を引き起こす可能性があります。
*   **新規クラスタ作成・手動アップグレード:** 今後GKEクラスタを新規作成したり、既存クラスタを手動でアップグレードする際には、新しいバージョンが選択肢として提供され、非推奨になったバージョンは選択できなくなります。
*   **自動アップグレードの挙動:** GKEクラスタが自動アップグレードを有効にしている場合、設定されたメンテナンスウィンドウに従い、クラスタコントロールプレーンおよびノードが新しいターゲットバージョン（マイナーまたはパッチ）に自動的にアップグレードされる可能性があります。マイナーバージョンアップグレードにはKubernetes APIの変更や非互換性が含まれる場合があるため、アプリケーションへの影響を確認する必要があります。
*   **Google Cloud Composer への影響:** Google Cloud Composer はGKEクラスタを利用していますが、ComposerのGKEバージョンはComposerのバージョン（今回はComposer version 2.7.1, Airflow version 2.7.3）に紐付いています。今回のGKEリリースノートで言及されているGKEバージョン（1.30.x ～ 1.36.x）は、Composer 2.7.1が現在使用しているGKEバージョンと異なる可能性が高いです（通常Composerはより安定した古いGKEバージョンをしばらく使用します）。そのため、このGKEバージョン更新が直ちにComposerクラスタに影響を与える可能性は低いですが、Composerが将来的にこれらのGKE新バージョンをサポートする際に、アプリケーションやAirflow DAGsの互換性確認が必要になることがあります。

対処方法：

1.  **GKEクラスタのバージョン確認:** 現在稼働中のGKEクラスタおよびGoogle Cloud Composerが利用しているGKEクラスタのバージョンが、今回非推奨とされたバージョンリストに含まれていないか確認してください。
    *   `gcloud container clusters list --project=<PROJECT_ID>`
    *   `gcloud composer environments describe <ENVIRONMENT_NAME> --location=<LOCATION> --project=<PROJECT_ID>` (GKEバージョンは `config.nodeConfig.machineType` などから推測できる場合もありますが、正確なGKEバージョンはComposerの公式ドキュメントやGoogle Cloudサポートへ問い合わせるのが確実です。)
2.  **アップグレード計画の策定:** 非推奨バージョンを使用しているGKEクラスタがある場合、**90日以内にサポート対象のGKEバージョンへのアップグレード計画を策定し、実行してください。** アップグレード前に、開発/ステージング環境で十分なアプリケーション互換性テストを実施し、Breaking Changeがないか確認することが重要です。
3.  **自動アップグレードポリシーの確認:** GKEクラスタの自動アップグレードが有効になっている場合、メンテナンスウィンドウやメンテナンス除外設定が適切に構成されているか確認し、予期せぬアップグレードによるサービス影響を防ぐようにしてください。
4.  **新規クラスタデプロイの考慮:** 今後GKEクラスタを新規デプロイする場合や手動アップグレードを行う際は、新しいGKEバージョンの中からプロジェクトの要件に合った安定バージョンを選択してください。

用語説明：
*   **GKE Release Channels (GKE リリースチャネル):** GKEクラスタのKubernetesバージョンと機能更新のリリース頻度と安定性を示すモデルです。Stable、Regular、Rapid、Extendedなどのチャネルがあり、それぞれ更新の速さと安定性のバランスが異なります。
*   **Default Version (デフォルトバージョン):** GKEクラスタを新規作成する際に、明示的にバージョンを指定しない場合に自動的に選択される推奨バージョンです。
*   **Deprecated (非推奨):** 将来的にサポートが終了し、利用できなくなる予定の機能やバージョンを指します。通常、一定の猶予期間が設けられ、代替手段への移行が推奨されます。
*   **Automatic Upgrades (自動アップグレード):** GKEがコントロールプレーンやノードのKubernetesバージョンを自動的に最新のパッチバージョンまたはマイナーバージョンに更新する機能です。
*   **Maintenance Window (メンテナンスウィンドウ):** GKEクラスタの自動メンテナンス（アップグレードなど）が許可される時間帯を指定する設定です。これにより、ビジネスへの影響を最小限に抑えることができます。
*   **Minor Version (マイナーバージョン):** Kubernetesのバージョン番号の2番目の数字（例: v1.**35**.5-gke.1241004）。通常、新機能の追加や後方互換性のない変更（Breaking Change）が含まれる可能性があります。
*   **Patch Version (パッチバージョン):** Kubernetesのバージョン番号の3番目の数字（例: v1.35.**5**-gke.1241004）。主にバグ修正やセキュリティパッチが含まれ、通常は後方互換性が維持されます。