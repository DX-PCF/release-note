
# Title: December 05, 2025 
Link: https://docs.cloud.google.com/release-notes#December_05_2025<br>
はい、承知いたしました。Google Cloudのリリースノートを元に、構築済みサービスへの影響有無を専門的な言葉遣いと書式で調査し、回答します。

---

# Apigee X

## Announcement
原文: On December 5th, 2025, we released an updated version of Apigee.
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：Apigeeの新しいバージョンがリリースされました。このリリースは2025年12月5日に開始され、すべてのGoogle Cloudゾーンで展開が完了するまでに4営業日以上かかる場合があります。展開が完了するまでは、新しい機能や修正がお客様のApigeeインスタンスで利用できない可能性があります。

影響有無：影響なし。
理由：これは新しいバージョンの展開開始を知らせるアナウンスであり、既存の機能動作に直接的な変更や非互換性はありません。新機能や修正の適用には時間がかかる旨の注意喚起です。

対処方法：ユーザー側での即座の対応は不要です。新機能や修正の利用を検討している場合は、展開状況を適宜確認してください。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **388271708** | **Security fix for Apigee infrastructure** This addresses the following vulnerability:- CVE-2025-13426Fixed an issue with the JavaCallout policy that could result in remote code execution. |

説明：Apigeeインフラストラクチャにおけるセキュリティ上の修正が実施されました。具体的には、JavaCalloutポリシーにおけるリモートコード実行（RCE）の脆弱性（CVE-2025-13426）が修正されました。

影響有無：影響なし（むしろ改善）。
理由：セキュリティ脆弱性の修正であり、システムが自動的に更新されるため、ユーザー側での追加の対応は不要です。セキュリティが強化されます。

対処方法：なし。この修正はGoogle Cloudによって自動的に適用されます。

用語説明：
*   **JavaCalloutポリシー**: ApigeeのAPIプロキシ内でカスタムのJavaコードを実行することを可能にするポリシーです。これにより、標準のApigee機能では実現できない複雑なロジックを実装できます。
*   **リモートコード実行 (RCE - Remote Code Execution)**: 攻撃者が遠隔地からシステム上で任意のコードを実行できる脆弱性の種類を指します。RCE脆弱性が存在すると、システムが完全に侵害される危険性があります。
*   **CVE-2025-13426**: 共通脆弱性識別子（Common Vulnerabilities and Exposures）は、公開された情報セキュリティの脆弱性および露出に対して、共通の識別子を付与するシステムです。この番号は、特定の脆弱性を一意に識別するために使用されます。

---

# Google Kubernetes Engine (GKE)

GKEのリリースノートは、各リリースチャネル（Extended, Implicit General, Rapid, Regular, Stable）におけるバージョン更新に関するものです。Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) はGKE上で動作するため、基盤となるGKEのバージョンアップはComposerの安定性や互換性に影響を与える可能性があります。一般的にGoogle Cloud ComposerはGKEのStableまたはRegularチャンネルを利用することが多いため、特にこれらのチャンネルの変更に注意が必要です。

## Changed (Extended channel)
原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.33.5-gke.1308000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
    - 1.28.15-gke.3202000
    - 1.29.15-gke.2520000
    - 1.30.14-gke.1760000
    - 1.31.13-gke.1139000
    - 1.31.13-gke.1454000
    - 1.32.9-gke.1239000
    - 1.32.9-gke.1548000
    - 1.33.5-gke.1791000
    - 1.34.1-gke.2909002
    - 1.34.1-gke.3084002
- The following versions are no longer available in the Extended channel:
    - 1.28.15-gke.2767000
    - 1.28.15-gke.2793000
    - 1.28.15-gke.2966000
    - 1.28.15-gke.3188000
    - 1.29.15-gke.2002000
    - 1.29.15-gke.2085000
    - 1.29.15-gke.2236000
    - 1.29.15-gke.2505000
    - 1.30.14-gke.1349000
    - 1.30.14-gke.1408000
    - 1.30.14-gke.1525000
    - 1.30.14-gke.1746000
    - 1.31.13-gke.1040000
    - 1.31.13-gke.1123000
    - 1.32.9-gke.1130000
    - 1.32.9-gke.1207000
    - 1.33.5-gke.1201000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.27 to 1.28.15-gke.3096000
        - 1.28 to 1.29.15-gke.2380000
        - 1.29 to 1.30.14-gke.1658000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.28 to 1.28.15-gke.3096000
        - 1.29 to 1.29.15-gke.2380000
        - 1.30 to 1.30.14-gke.1658000
        - 1.31 to 1.31.13-gke.1139000
        - 1.32 to 1.32.9-gke.1239000
        - 1.33 to 1.33.5-gke.1308000
        - 1.34 to 1.34.1-gke.2909002

説明：GKEのExtendedチャンネルにおいて、新規クラスター作成時のデフォルトバージョンが`1.33.5-gke.1308000`になりました。このチャンネルで利用可能なバージョンリストが更新され、一部のバージョンは利用不可になりました。また、このチャンネルのクラスターに対する自動アップグレードのターゲットバージョンが更新されました。これにより、マイナーバージョンアップグレードおよびパッチバージョンアップグレードの新しい目標バージョンが設定されています。

影響有無：影響あり。
理由：
*   **既存クラスター**: ExtendedチャンネルでGKEクラスターを運用している場合、自動アップグレードが有効であれば、クラスターのコントロールプレーンおよびノードが新しいターゲットバージョンに自動的にアップグレードされる可能性があります。これにより、一時的なダウンタイムやアプリケーションの互換性問題が発生する可能性があります。
*   **新規クラスター**: 新規クラスターを作成する際のデフォルトバージョンが変更されるため、意図せず新しいバージョンで作成される可能性があります。

対処方法：
1.  **GKEクラスターのチャンネル確認**: 現在運用中のGKEクラスターがExtendedチャンネルを利用しているか確認してください。
2.  **メンテナンスウィンドウの確認**: 自動アップグレードが有効な場合、設定しているメンテナンスウィンドウやメンテナンス除外期間が適切に機能しているか確認し、業務に影響が出ない時間帯にアップグレードが行われるように調整してください。
3.  **アプリケーションの互換性テスト**: 新しいGKEバージョン（特にマイナーバージョンアップグレード）に備えて、ステージング環境などでアプリケーションの互換性テストを実施し、問題がないことを確認することが強く推奨されます。
4.  **Google Cloud Composer2の互換性確認**: Google Cloud Composer2がExtendedチャンネルのGKEを基盤としている場合、Composerのリリースノートや互換性マトリックスを参照し、新しいGKEバージョンがサポート対象であることを確認してください。必要に応じてComposerのアップグレードも検討してください。

用語説明：
*   **Extended channel (拡張チャネル)**: GKEのリリースチャネルの一つで、Regularチャンネルよりも新しい機能が提供されますが、Stableチャンネルほどではない安定性を持ちます。より長いサポート期間が特徴です。
*   **デフォルトバージョン**: 新規GKEクラスターを作成する際に、特定のバージョンを指定しない場合に自動的に適用されるGKEのバージョンです。
*   **自動アップグレードターゲット**: GKEがクラスターを自動的にアップグレードする際に目指す目標バージョンです。コントロールプレーンとノードの両方に適用されます。
*   **マイナーバージョンアップグレード**: Kubernetesのマイナーバージョン番号（例: v1.28からv1.29）の変更を伴うアップグレードです。Kubernetesの新しいAPIバージョンや機能の変更が含まれることがあり、互換性に影響が出る可能性があります。
*   **パッチバージョンアップグレード**: Kubernetesのパッチバージョン番号（例: v1.28.14からv1.28.15）の変更を伴うアップグレードです。主にバグ修正、セキュリティ修正、パフォーマンス改善などが含まれ、通常は後方互換性が維持されます。
*   **メンテナンス除外 (Maintenance Exclusions)**: GKEクラスターの自動メンテナンス（自動アップグレードなど）が実行されない期間を一時的に設定する機能です。

## Changed (Implicit General Channel)
原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.33.5-gke.1308000 is now the default version for cluster creation.
- The following versions are now available:
    - 1.31.14-gke.1045000
    - 1.32.9-gke.1592000
    - 1.33.5-gke.1894000
    - 1.34.1-gke.2909002
    - 1.34.1-gke.3084002
    - 1.34.1-gke.3355001
    - 1.34.1-gke.3403001
- The following node versions are now available:
    - 1.28.15-gke.3202000
    - 1.29.15-gke.2520000
    - 1.30.14-gke.1760000
    - 1.31.14-gke.1045000
    - 1.32.9-gke.1592000
    - 1.33.5-gke.1894000
    - 1.34.1-gke.2909002
    - 1.34.1-gke.3084002
    - 1.34.1-gke.3355001
    - 1.34.1-gke.3403001
- The following versions are no longer available:
    - 1.31.13-gke.1008000
    - 1.31.13-gke.1040000
    - 1.31.13-gke.1123000
    - 1.31.14-gke.1033000
    - 1.32.9-gke.1092000
    - 1.32.9-gke.1130000
    - 1.32.9-gke.1207000
    - 1.32.9-gke.1575000
    - 1.33.5-gke.1080000
    - 1.33.5-gke.1350000
    - 1.33.5-gke.1521000
    - 1.33.5-gke.1697000
    - 1.34.1-gke.1829001
    - 1.34.1-gke.2037002
    - 1.34.1-gke.2541000
    - 1.34.1-gke.2909000
    - 1.34.1-gke.2980000
    - 1.34.1-gke.3084001
    - 1.34.1-gke.3225000
    - 1.34.1-gke.3355000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.30 to 1.31.13-gke.1139000
        - 1.31 to 1.32.9-gke.1239000
        - 1.32 to 1.33.5-gke.1162000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.31 to 1.31.13-gke.1139000
        - 1.32 to 1.32.9-gke.1239000
        - 1.33 to 1.33.5-gke.1162000
        - 1.34 to 1.34.1-gke.2909002

説明：GKEのバージョン更新です。新規クラスター作成時のデフォルトバージョンが`1.33.5-gke.1308000`に変更され、利用可能・利用不可となったバージョンリストが更新されました。これには特定のチャンネルの指定はありませんが、他のチャンネルの記述とは異なるバージョンが含まれます。また、ノードバージョンも更新され、自動アップグレードのターゲットバージョンも更新されました。

影響有無：影響あり。
理由：
*   **既存クラスター**: GKEクラスターを運用している場合、自動アップグレードが有効であれば、クラスターのコントロールプレーンおよびノードが新しいターゲットバージョンに自動的にアップグレードされる可能性があります。これにより、一時的なダウンタイムやアプリケーションの互換性問題が発生する可能性があります。
*   **新規クラスター**: 新規クラスターを作成する際のデフォルトバージョンが変更されるため、意図せず新しいバージョンで作成される可能性があります。

対処方法：
1.  **GKEクラスターのチャンネル確認**: 現在運用中のGKEクラスターがどのチャンネルを利用しているか確認してください。
2.